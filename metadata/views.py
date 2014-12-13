from datetime import datetime

from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from metadata.models import Action, Project
from metadata.forms import ProjectForm

# Create your views here.
def dashboard(request):
	return render (request, 'dashboard.html', {})

def project_form(request):
	project_form = ProjectForm()
	context = {
		'project_form': project_form
	}
	return render(request,'project_form.html', context)

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