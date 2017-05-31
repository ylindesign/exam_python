from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse

from django.contrib import messages
from .models import User

def index(request):
	if 'name' in request.session:
		return redirect('wish:wish')
	return render(request, 'login/index.html')

def register(request):
	person = {
		'name': request.POST['name'],
		'username': request.POST['username'],
		'password': request.POST['password'],
		'conf_pw': request.POST['conf_pw'],
		'hired': request.POST['hired'],
	}

	if request.method != "POST":
		messages.add_message(request, messages.ERROR, "Cant have an empty form")
		return redirect("/")

	response = User.objects.Regis(person)

	if response['status'] == False:
		for error in response['errors']:
			messages.add_message(request, messages.ERROR, error)
		return redirect("/")
	else:
		messages.add_message(request, messages.SUCCESS, "You have registered!" )
		request.session['name'] = person['name']
		request.session['id'] = response['person'].id
	return redirect('wish:wish')

def login(request):
	if request.method == "POST":
		response = User.objects.Login(request.POST)
		if response['status'] == True:
			print "name: ", response['user'].name
			print "id: ", response['user'].id
			request.session['name'] = response['user'].name
			request.session['id'] = response['user'].id
		return redirect('wish:wish')
	else:
		for error in response['errors']:
			messages.error(request, error)
	return redirect('/')

def logout(request):
	request.session.flush()
	return redirect('/')
 