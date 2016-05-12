from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
	article_title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	article_author = models.CharField(max_length=100)
	article_content = models.TextField()

	def __str__(self):
		return self.article_title