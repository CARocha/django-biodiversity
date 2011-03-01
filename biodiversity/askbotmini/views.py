from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from tagging.models import Tag, TaggedItem
from forms import *
from models import *
import datetime
import operator

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
    return render_to_response('askbotmini/index.html', locals(), context_instance=RequestContext(request))

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
#        if form.is_valid():
        obj = Question()
        obj.question = request.POST['question']
        obj.description = request.POST['description']
        obj.user = request.user
        obj.views = 0
        obj.date_created = datetime.datetime.now()
        obj.tags = request.POST['tags']
        obj.save()
        return HttpResponseRedirect('/askbot/')
    else:
        form = AskForm()
    return render_to_response('askbotmini/ask_question.html', RequestContext(request, locals()))

@login_required
def view_question(request, id):
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
    return render_to_response('askbotmini/tagged_in.html', RequestContext(request, locals()))