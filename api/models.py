from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class Post(TimeStampedModel, SoftDeletableModel):
	title 				= models.CharField(max_length=50, null=False, blank=True)
	body 				= models.TextField(max_length=5000, null=False, blank=True)
	date_published 		= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 		= models.DateTimeField(auto_now=True, verbose_name="date updated")
	slug 				= models.SlugField(blank=True, unique=True)
	def __str__(self):
		return self.title


class MrOlimpya(TimeStampedModel, SoftDeletableModel):
	full_name 			= models.CharField(max_length=50, verbose_name="Nombre completo")
	biography 			= models.TextField(max_length=5000, null=False, blank=True, verbose_name="Biografía")
	weight 				= models.CharField(max_length=50, verbose_name="Peso")
	height 				= models.CharField(max_length=50, verbose_name="Altura")
	age 		        = models.CharField(max_length=50, verbose_name="Edad")
	phrases 		    = models.TextField(max_length=5000, null=False, blank=True, verbose_name="Frases Comunes")
	date_published 		= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 		= models.DateTimeField(auto_now=True, verbose_name="date updated")
	slug 				= models.SlugField(blank=True, unique=True)
	def __str__(self):
		return self.full_name