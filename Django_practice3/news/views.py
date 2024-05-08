from django.shortcuts import render
from . import models


def index(request):
    news = models.News.objects.all()

    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})
