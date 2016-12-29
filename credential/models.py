from django.db import models
from user.models import User


class SocialCredential(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	user_name = models.CharField(max_length=50, blank=True)
	password = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=50, blank=True)
	phone_number = models.CharField(max_length=30, blank=True)
	description = models.CharField(max_length=250, blank=True)

	def __str__(self):
		return self.user.name + ' ' + self.description
