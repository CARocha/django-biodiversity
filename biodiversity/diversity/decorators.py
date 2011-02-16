from django.http import HttpResponseRedirect
def session_required(f):
    def check_session(request, **kwargs):
        if 'activa' not in request.session.keys():
            return HttpResponseRedirect('/')
        return f(request, **kwargs)
    return check_session
