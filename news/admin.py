from django.contrib import admin
from django.db import models
#from django_admin_bootstrapped.widgets import GenericContentTypeSelect
# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
	search_fields = ('article_title', 'article_content',) 
	class Media:
		js=('/media/js/tiny_mce/tiny_mce.js',
			'/media/js/textareas.js'
		)

admin.site.register(Article,ArticleAdmin)