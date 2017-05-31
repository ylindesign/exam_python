from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse

from django.contrib import messages
from .models import Wish
from ..login.models import User

def wish(request):
	context = {
		'wishes': Wish.objects.all(),
		# 'total_likes': Secret.objects.annotate(total_likes=Count('likes')),
	}
	return render(request, 'wish/wish.html', context)

def create(request):
	return render(request, 'wish/create.html')
	# return render(request, 'wish/create.html')

def add(request):
	if request.method == 'POST':
		new_wish = request.POST['wish']
		# print 'here is the wish: ', request.POST['wish']
		person = User.objects.get(id=request.session['id'])
		# person = int(request.session['id'])
		# print 'person id right now: ', request.session['id']
		response = Wish.objects.Valid(new_wish)
	if response['status']:
		Wish.objects.AddWish(new_wish, person)
	else:
		for error in response['errors']:
			messages.error(request, error)
		return redirect('wish:create')
	return redirect('wish:wish')

def item(request, id):
	context = {
		# 'something': id
		'item': Wish.objects.filter(id=id),
	}
	print context
	return render(request, 'wish/item.html', context)

def copy(request, id, user):
	new_wish = Wish.objects.get(id=id).item
	# print "Wish is: ", new_wish
	person = User.objects.get(id=request.session['id'])
	Wish.objects.CopyWish(new_wish, person, user)
	return redirect('wish:wish')

def delete(request, id):
	new_wish = Wish.objects.get(id=id).item
	# print "new wishes name in views: ", new_wish
	person = User.objects.get(id=request.session['id'])
	Wish.objects.DeleteWish(new_wish, person)
	return redirect('wish:wish')

def remove(request, id, add):
	new_wish = Wish.objects.get(id=id).item
	person = User.objects.get(id=request.session['id'])
	Wish.objects.RemoveWish(new_wish, person, add)
	return redirect('wish:wish')
