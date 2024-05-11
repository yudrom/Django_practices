from django.shortcuts import render
from . import models


def index(request):
    news = models.News.objects.all()
    categories = models.Category.objects.all()
    context = {
        'news': news,
        'categories': categories,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = models.News.objects.filter(category=category_id)
    categories = models.Category.objects.all()
    category = models.Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category,
        'title': category
    }
    return render(request, template_name='news/category.html', context=context)


def get_absolute_url(request):
    pass
