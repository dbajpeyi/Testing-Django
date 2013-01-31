from django.db import models
import datetime

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200,unique=True)
	body = models.TextField()
	posted = models.DateField(default = datetime.datetime.now())
	
	def __unicode__(self):
		return self.title

class Category(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	posts = models.ManyToManyField(Blog)

	def __unicode__(self):
		return self.title
