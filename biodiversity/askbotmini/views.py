import operator
import thread
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from forms import *
from models import *
from tagging.models import Tag
from tagging.models import TaggedItem

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
            TaggedItems = TaggedItem.objects.get_by_model(Question, rtag.name)
            if not rtag.items.all().count() == 0:
                li = []
                for it in rtag.items.all():
                    if it.object:
                        li.append(it)
                tags.append({'name':rtag.name, 'count': len(li)})
            for item in TaggedItems:
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
                thread.start_new_thread(notify_all, (obj,))
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

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = Answer()
            answer.question = question
            answer.answer = form.cleaned_data['answer']
            answer.fecha = datetime.datetime.now()
            answer.user = request.user
            answer.save()
            #notify_user(question, answer)
            thread.start_new_thread(notify_user, (question, answer))
            return HttpResponseRedirect('/foro/questions/%s/?ansid=%s' % (question.id, answer.id))
    else:
        form = AnswerForm()

    ansid = request.GET.get('ansid', '')

    return render_to_response('askbotmini/view_question.html', RequestContext(request, locals()))

@login_required
def edit_answer(request, id):
    tags = Tag.objects.usage_for_model(Question, counts=True)
    tags.sort(key=operator.attrgetter('count'), reverse=True)
    answer = get_object_or_404(Answer, id=id)

    if answer.user != request.user:
        return HttpResponse('<h2>Acceso Denegado</h2>')

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/foro/questions/%s/?ansid=%s' % (answer.question.id, answer.id))
    else:
        form = AnswerForm(instance=answer)

    return render_to_response('askbotmini/edit_answer.html', RequestContext(request, locals()))

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
    users = User.objects.all().exclude(username='admin').exclude(username=question.user.username)
    contenido = render_to_string('askbotmini/notify_new_question.txt', {'question': question,
                                 'url': '%s%s' % (site, question.id),
                                 'url_answer': '%s%s/#answer' % (site, question.id),
                                 })
    for user in users:
        if user.email:
            send_mail('Nueva pregunta', contenido, 'develop@simasni.org', [user.email, ])

def notify_user(question, answer):
    site = 'http://localhost:8000/foro/questions/'
    
    text_content = render_to_string('askbotmini/notify_new_answer_text.txt', {'question': question,
                                 'url': '%s%s' % (site, question.id),
                                 'url_answer': '%s/#%s' % (site, answer.id),
                                 'answer': answer
                                 })
    html_content = render_to_string('askbotmini/notify_new_answer.txt', {'question': question,                                 
                                 'url_answer': '%s%s/?ansid=%s' % (site, question.id, answer.id),
                                 'answer': answer
                                 })

    msg = EmailMultiAlternatives('1 Pregunta tiene 1 Respuesta nueva', text_content, 'develop@simasni.org', [question.user.email, ])
    msg.attach_alternative(html_content, "text/html")
    msg.send()  