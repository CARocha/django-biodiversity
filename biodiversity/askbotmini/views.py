from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import *
from models import *
import datetime

def index(request):
    questions = Question.objects.all().order_by('-last_answer_date')
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