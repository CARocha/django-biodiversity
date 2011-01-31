from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

import datetime

class Categories(models.Model):
    titulo = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.titulo

    class Meta:
        verbose_name = 'Categorias'
        verbose_name_plural = 'Categorias'


class Forum(models.Model):
    category = models.ForeignKey(Categories)
    titulo = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=100, editable=False)
    descripcion = models.TextField()
    threads = models.IntegerField(default=0, editable=False)
    posts = models.IntegerField(default=0, editable=False)

    def _get_forum_latest_post(self):
        """Obtiene el ultimo post para este foro"""
        if not hasattr(self, '__forum_latest_post'):
            try:
                self.__forum_latest_post = Post.objects.filter(forum__pk=self.id).latest('time')
            except Post.DoesNotExist:
                try:
                    self.__forum_latest_post = Thread.objects.filter(forum__pk=self.id).latest('time')
                except Thread.DoesNotExist:
                    self.__forum_latest_post = None

        return self.__forum_latest_post
    forum_latest_post = property(_get_forum_latest_post)

    def save(self, force_insert=False, force_update=False):
        try:
	    f = Forum.objects.get(pk=self.id)
	    super(Forum, self).save(force_insert, force_update)
	except:
	    n = Forum.objects.all().count()
	    self.slug = str(n) + '-'  + slugify(self.titulo)
	    super(Forum, self).save(force_insert, force_update)


    def __unicode__(self):
        return u'%s' % self.titulo

    class Meta:
        verbose_name = 'Foro'
        verbose_name_plural = 'Foros'

class Thread(models.Model):
    forum = models.ForeignKey(Forum)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    author = models.ForeignKey(User)
    posts = models.IntegerField(default=0, verbose_name='Posts', editable=False)
    visto = models.IntegerField(default=0, verbose_name='Visto')
    slug = models.CharField(unique=True, max_length=100, editable=False)
    time = models.DateTimeField(blank=True, null=True)
    latest_post_time = models.DateTimeField(blank=True, null=True, verbose_name='Latest Post Time')
    body = models.TextField()

    def _get_thread_latest_post(self):
        """Obtiene el ultimo post para este tema"""
        if not hasattr(self, '__thread_latest_post'):
            try:
                self.__thread_latest_post = Post.objects.filter(thread__pk=self.id).latest('time')
            except Post.DoesNotExist:
                self.__thread_latest_post = self

        return self.__thread_latest_post
    thread_latest_post = property(_get_thread_latest_post)

    class Meta:
        ordering = ["-time"]
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.time = datetime.datetime.now()

        f = self.forum
        f.threads = f.thread_set.count()+1
        f.save()
	try:
	    f = Thread.objects.get(pk=self.id)
	except:
	    n = Thread.objects.all().count()
            self.slug = str(n) + '-' + slugify(self.titulo)
	    super(Thread, self).save(force_insert, force_update)

    def delete(self):
        super(Thread, self).delete()
        f = self.forum
        f.threads = f.thread_set.count()
        f.posts = Post.objects.filter(thread__forum__pk=f.id).count()
        f.save()

    def __unicode__(self):
        return u'%s' % self.titulo

class Post(models.Model):
    forum = models.ForeignKey(Forum)
    thread = models.ForeignKey(Thread)
    author = models.ForeignKey(User)
    body = models.TextField()
    time = models.DateTimeField(blank=True, null=True)

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.time = datetime.datetime.now()
        super(Post, self).save(force_insert, force_update)

        t = self.thread
        t.latest_post_time = t.post_set.latest('time').time
        t.posts = t.post_set.count()
        t.save()

        f = self.thread.forum
        f.threads = f.thread_set.count()
        f.posts = Post.objects.filter(thread__forum__pk=f.id).count()
        f.save()

    def delete(self):
        try:
            latest_post = Post.objects.exclude(pk=self.id).latest('time')
            latest_post_time = latest_post.time
        except Post.DoesNotExist:
            latest_post_time = None

        t = self.thread
        t.posts = t.post_set.exclude(pk=self.id).count()
        t.latest_post_time = latest_post_time
        t.save()

        f = self.thread.forum
        f.posts = Post.objects.filter(thread__forum__pk=f.id).exclude(pk=self.id).count()
        f.save()

        super(Post, self).delete()


    class Meta:
        ordering = ["time"]
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

    def __unicode__(self):
        return u"Respuestas en %s" % self.thread.titulo

