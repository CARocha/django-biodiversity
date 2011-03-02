from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.models import User
from tagging.models import Tag, TaggedItem
from forms import *
from models import *
import operator
import datetime

def index(request):
    request.session['flag'] = 'foro'
    barra_foro = 'index'
    questions = Question.objects.all().order_by('-last_answer_date')

    #valorando si muestra solo las ultimas preguntas
    tab = request.GET.get('tab', '')
    if tab == 'latest':
        barra_foro = 'latest'
        questions = Question.objects.all().order_by('-date_created')

    tags = Tag.objects.usage_for_model(Question, counts=True)
    tags.sort(key=operator.attrgetter('count'), reverse=True)  

    query = request.GET.get('q', '')
    if query:
        result_questions = Question.objects.filter(question__icontains=query)
        result_tags = Tag.objects.filter(name__icontains=query)
        lista = []
        tags = []
        for n in result_questions:
            lista.append(n)
        for rtag in result_tags:
            if not rtag.items.all().count() == 0:
                tags.append({'name':rtag.name, 'count': rtag.items.all().count()})
            for item in TaggedItem.objects.get_by_model(Question, rtag.name):
                lista.append(item)
        tags.sort(key=operator.itemgetter('count'), reverse=True)
        questions = list(set(lista))        

    return render_to_response('askbotmini/index.html', locals(), context_instance=RequestContext(request))

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            obj = Question()
            obj.question = request.POST['question']
            obj.description = request.POST['description']
            obj.user = request.user
            obj.views = 0
            obj.date_created = datetime.datetime.now()
            obj.tags = request.POST['tags']
            obj.save()
            if form.cleaned_data['notify']:
                notify_all(obj)
            return HttpResponseRedirect('/foro/?tab=latest')
    else:
        form = AskForm()
    return render_to_response('askbotmini/ask_question.html', RequestContext(request, locals()))

@login_required
def edit_question(request, id):
    question = get_object_or_404(Question, id=int(id))    
    if not question.user == request.user:
        return HttpResponse('<h1>Permiso denegado</h1>')

    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():            
            question.question = request.POST['question']
            question.description = request.POST['description']
            question.tags = request.POST['tags']
            question.save()
            return HttpResponseRedirect('/foro/questions/%s' % question.id)
    else:
        form = AskForm(instance=question)
    return render_to_response('askbotmini/ask_question.html', RequestContext(request, locals()))

@login_required
def view_question(request, id):
    tags = Tag.objects.usage_for_model(Question, counts=True)
    tags.sort(key=operator.attrgetter('count'), reverse=True)
    question = get_object_or_404(Question, id=int(id))
    user_ip = request.META['REMOTE_ADDR']
    try:
        vista = View.objects.get(question=question, ip=user_ip)
    except:
        vista = View()
        vista.question = question
        vista.ip = user_ip
        vista.save()
        question.views = question.views + 1
        question.save()

    return render_to_response('askbotmini/view_question.html', RequestContext(request, locals()))

@login_required
def tagged_in(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    questions = TaggedItem.objects.get_by_model(Question, tag.name).order_by('-last_answer_date')

    tags = Tag.objects.usage_for_model(Question, counts=True)
    tags.sort(key=operator.attrgetter('count'), reverse=True)
    return render_to_response('askbotmini/tagged_in.html', RequestContext(request, locals()))

#este sera el hilo para mandar mails
def notify_all(question):
    site = 'http://localhost:8000/foro/questions/'
    users = User.objects.all().exclude(username='admin')
    contenido = render_to_string('askbotmini/notify_new_question.txt', {'question': question,
                        'url': '%s%s' % (site, question.id),
                        'url_answer': '%s%s/#answer' % (site, question.id),
                        })
    for user in users:
        if user.email:
            send_mail('Nueva pregunta', contenido, 'develop@simasni.org', [user.email, ])
