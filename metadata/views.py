from datetime import datetime

from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from metadata.models import Action, Project

# Create your views here.
@login_required
def dashboard(request):
	projects = Project.objects.filter(assigned_users__in=[request.user])
	actions = Action.objects.filter(project__in=projects)
	context = {
		'actions':actions,
		'user': request.user,
	}
	return render (request, 'dashboard.html', context)

@login_required
def projects(request):
	context = {
	}
	return render (request, 'projects.html', context)

@login_required
def calendar(request):
	context = {
	}
	return render (request, 'calendar.html', context)

@login_required
def settings(request):
	context = {
	}
	return render (request, 'settings.html', context)

def auth_login(request):
	if request.user.is_authenticated():
		return redirect('dashboard')
	else:
		c = {}
		c.update(csrf(request))
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username = username, password = password)
			if user is not None:
			    if user.is_active:
			        print("User is valid, active and authenticated")
			        login(request, user)
			        return HttpResponseRedirect(reverse('dashboard'))
			    else:
			    	#TODO: MAKE THIS PAGE
			        return HttpResponse("The password is valid, but the account has been disabled!")
			else:
			    # TODO: MAKE THIS PAGE
			    return HttpResponse("The username and password were incorrect.")
		else:
			return render(request, 'login.html', {})

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))