from datetime import datetime, timedelta
from django.db import models
from django.utils import timezone


# Create your models here.

class Paste(models.Model):
	paste_name = models.CharField(max_length =200, null=False)
	paste_content = models.TextField(null = False)
	paste_url = models.CharField(max_length=200, null=False)
	created = models.DateTimeField(auto_now_add=True)
	date_of_expiry = models.DateField()
	def __str__(self):
		return self.paste_name

	def is_expired(self):
		if (self.date_of_expiry-datetime.today().date()).days<=0:
			return True
		else:
			return False