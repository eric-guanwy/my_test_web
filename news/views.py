from django.shortcuts import render

# Create your views here.
from .models import Article

def index(request):
	latest_article_list = Article.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('news/index.html')
	#output = ', '.join([a.article_title for a in latest_article_list])
	context = {
		'latest_article_list':latest_article_list,
	}
	return render(request,'news/index.html',context)

def detail(request,article_id):
	article = Article.objects.get(pk=article_id)
	context = {
		'article':article
	}
	return render(request,'news/detail.html',context)

def article(request):
	article_list = Article.objects.order_by('-pub_date')[:20]
	context = {
		'article_list':article_list,
	}
	return render(request,'news/article.html',context)
