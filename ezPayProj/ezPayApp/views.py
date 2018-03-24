# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ezPayApp.models import *
from ezPayApp.capOne import *
# Create your views here.

def loginpage(request):
	if request.user and request.user.is_authenticated:
		return HttpResponseRedirect(reverse('home'))
	context={}
	errors=[]

	if request.method == 'GET':
		schools = School.objects.all()
		context['schools'] = schools
   		return render(request,'login.html', context)

   	schId = request.POST.get('sch_id')
   	sch = School.objects.get(id = schId)

   	return HttpResponseRedirect(reverse('schlogin'))


def schLogin(request):
	
	context = {}
	if request.method == 'GET':
		return render(request, 'sch_login.html', context)
	else:
		return HttpResponseRedirect(reverse('home'))

def home(request):
	user = PayUser.objects.get(id = request.user)
	context['user'] = user
	context['accounts'] = get_eligible_accounts()

	return render(request, 'home.html', context)






