from django.contrib import admin
from django.db import models
#from django_admin_bootstrapped.widgets import GenericContentTypeSelect
# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'article_content':
            #kwargs['widget'] = GenericContentTypeSelect            
            pass
        return super(ArticleAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Article,ArticleAdmin)