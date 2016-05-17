from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
#from tinymce import models as tinymce_models

@python_2_unicode_compatible
# Create your models here.

class Article(models.Model):
	article_title = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	article_author = models.CharField(max_length=200)
	article_content = models.TextField()
	photo = models.ImageField('upload picture',upload_to='photos',null=True,blank=True)

	def __str__(self):
		return self.article_title