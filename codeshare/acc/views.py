__author__ = 'Shaurya'

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib import auth
from codeshare.acc.forms import SignupForm,LoginForm


def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/acc/login/")
    else:
        form = SignupForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response("signup.html",args)

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    args = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if authentication(request):
                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect("/")
            else:
                args['invalid']=True
    else:
        form = LoginForm()
    args.update(csrf(request))
    args['form'] = form
    args['next'] = request.GET.get('next', default='')
    return render_to_response("login.html",args)

def authentication(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return True
    else:
        return False

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")