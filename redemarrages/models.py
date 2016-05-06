from django.db import models
from django.contrib import admin

# Create your models here.
class Redemarrage(models.Model):
	timestamp = models.DateTimeField()

class Application(models.Model):
	nom = models.DateTimeField()
	
admin.site.register(Redemarrage)