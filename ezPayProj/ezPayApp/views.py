# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ezPayApp.models import *
from ezPayApp.forms import *
from ezPayApp.capOne import *
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.forms import ModelForm

# Create your views here.
balance = 0.0
remaining = 1000.0
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
   	#sch = School.objects.get(id = schId)

   	return HttpResponseRedirect(reverse('schlogin'))


def schLogin(request):
	
	context = {}
	if request.method == 'GET':
		return render(request, 'sch_login.html', context)
	else:
		return HttpResponseRedirect(reverse('home'))

def home(request):
	setup_oauth()
	# user = PayUser.objects.get(stuId = request.user)
	# context['user'] = user
	context = {}
	
	accounts  = get_eligible_accounts()
	print(balance)
	context['balance'] = balance
	context['remaining'] = remaining
	context['accounts'] = accounts['accounts']
	context['form'] = TransferForm()
	context['form_heading'] = 'Transer funds'
	print(accounts)
	return render(request, 'home.html', context)


def shopping(request):
	global balance
	global remaining
	if request.GET.get('paybtn'):
		print('entered paybtn')
		balance += 339.99
		remaining -= 339.99
		print(balance)
	return render(request, 'shopping.html', {})

def transfer(request):
	form = TransferForm(request.POST)
	valid = form.is_valid()
	req = form.cleaned_data
	resp = initiate_transfer(req)
	print(resp)
	context = {}
	if 'description' in resp:
		context['errors'] = [resp['description']]
	elif 'transferRequestStatus' in resp and resp['transferRequestStatus'] == 'Scheduled':
		context['infomsgs'] = ['Scheduled with ID: '+resp['transferRequestId']]

	accounts  = get_eligible_accounts()
	context['accounts'] = accounts['accounts']
	context['balance'] = balance
	context['remaining'] = remaining
	context['form'] = TransferForm()
	context['form_heading'] = 'Transer funds'

	return render(request, 'home.html', context)