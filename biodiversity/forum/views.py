from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.http import *
import datetime
from forum.models import *
from forum.forms import *


def index(request):
    request.session['flag'] = 'foro'
    categorias = Categories.objects.all()
    total_post = Post.objects.all().count()
    total_topics = Thread.objects.all().count()
    total_users = User.objects.all().count()

    return render_to_response('forum/index.html', locals(),
                              context_instance=RequestContext(request))

def forum_list(request, slug):
    flag = 'foro'
    try:
        forum = Forum.objects.get(slug=slug)
    except ObjectDoesNotExist:
        Http404

    total_post = Post.objects.all().count()
    total_topics = Thread.objects.all().count()
    total_users = User.objects.all().count()

    return render_to_response('forum/forum_list.html', locals(),
                               context_instance=RequestContext(request))

def forum_detail(request, slug, t_slug):
    flag = 'foro'
    try:
        thread = Thread.objects.get(slug=t_slug)
        thread.visto = thread.visto+1
        thread.save()

        posts = thread.post_set.all()
    except ObjectDoesNotExist:
        Http404

    return render_to_response('forum/forum_detail.html', locals(),
                               context_instance=RequestContext(request))

@login_required(redirect_field_name='next')
def new_topic(request, slug):
    flag = 'foro'
    try:
        forum = Forum.objects.get(slug=slug)
    except ObjectDoesNotExist:
        Http404

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = Thread()
            topic.forum = forum
            topic.author = request.user
            topic.titulo = form.cleaned_data['titulo']
            topic.body = form.cleaned_data['body']
            topic.save()
            try:
                request.user.get_profile().mas_ranking()
                la = LastActivity()
                la.member = request.user.get_profile()
                la.tipo = 'abrio_foro'
                la.titulo = form.cleaned_data['titulo']
                la.url = 'http://bioversity.simasni.org/foro/'+slug+'/'+slugify(form.cleaned_data['titulo'])+'/'
                la.fecha = datetime.datetime.now()
                la.save()
            except:
                pass
            return HttpResponseRedirect('/foro/'+slug+'/')
    else:
        form = TopicForm()

    return render_to_response('forum/new_topic.html', locals(),
                              context_instance=RequestContext(request))

@login_required(redirect_field_name='next')
def topic_reply(request, slug, t_slug):
    flag = 'foro'
    try:
        forum = Forum.objects.get(slug=slug)
    except ObjectDoesNotExist:
        Http404

    try:
        thread = Thread.objects.get(slug=t_slug)
    except ObjectDoesNotExist:
        Http404

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.forum = forum
            post.thread = thread
            post.author = request.user
            post.body = form.cleaned_data['body']
            post.save()
            try:
                request.user.get_profile().mas_ranking()
                la = LastActivity()
                la.member = request.user.get_profile()
                la.tipo = 'respondio_foro'
                la.titulo = thread.titulo
                la.url = 'http://bioversity.simasni.org/foro/'+slug+'/'+t_slug+'/'
                la.fecha = datetime.datetime.now()
                la.save()
            except:
                pass
            return HttpResponseRedirect('/foro/'+slug+'/'+t_slug+'/')
    else:
        form = PostForm()

    return render_to_response('forum/reply.html', locals(),
                               context_instance=RequestContext(request))

