from __future__ import unicode_literals

from django.db import models
from ..login.models import User


class wishManager(models.Manager):
	def Valid(self, new_wish):
		response = {}
		errors = []
		if len(new_wish) < 1:
			errors.append('Wishes cannot be blank!')
		if len(new_wish) < 4:
			errors.append('Wishes should be more than 3 characters')
		if errors:
			response['status'] = False
			response['errors'] = errors
		else:
			response['status'] = True
		return response

	def AddWish(self, new_wish, person):
		self.create(item=new_wish, user=person)

	def CopyWish(self, new_wish, person, user):
		# print "new wish: ", new_wish
		# print "person", person
		# print "user", user
		self.create(item=new_wish, user=person, add=user)

	def DeleteWish(self, new_wish, person):
		# self.get(item=new_wish, user=person).delete()
		self.get(item=new_wish, user=person).delete()
	# def AddLike(self, user_id, secret_id):
	# 	this_user = User.objects.get(id=user_id)
	# 	this_secret = self.get(id=secret_id)
	# 	like = this_secret.like.add(this_user)
	# 	return True

	def RemoveWish(self, new_wish, person, add):
		# self.get(item=new_wish, user=person).delete()
		self.get(item=new_wish, user=person, add=add).delete()

class Wish(models.Model):
	item = models.TextField()
	user = models.ForeignKey(User, related_name = 'user_wish')
	add = models.TextField(default="no")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = wishManager()