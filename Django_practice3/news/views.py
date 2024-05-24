from django.shortcuts import render
from django.utils.timezone import now
from rest_framework.response import Response
from . import models, forms, serializers, filters
from django.views.generic import ListView, RedirectView, FormView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import News


def index(request):
    news = models.News.objects.all()
    categories = models.Category.objects.all()
    context = {
        'news': news,
        'categories': categories,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context)


class ClassBasedIndex(ListView):  # Классовое представление index
    model = models.News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        context['title'] = 'Список новостей'
        context['additional_info'] = now()
        context['filter'] = self.get_filters()
        return context

    def get_filters(self):
        return filters.NewsFilter(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs


def get_category(request, category_id):
    news = models.News.objects.filter(category=category_id)
    categories = models.Category.objects.all()
    category = models.Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category,
        'title': category,
    }
    return render(request, template_name='news/category.html', context=context)


class ClassGetCategory(ListView):  # Классовое представление get_category
    model = models.News
    template_name = 'news/category.html'
    context_object_name = 'news'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return models.News.objects.filter(category_id=category_id)

    def get_context_data(self, *kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        category_id = self.kwargs.get('category_id')
        context['category'] = models.Category.objects.get(pk=category_id)
        context['title'] = context['category']
        return context


class Redirect(RedirectView):
    query_string = True
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


class SimpleForm(FormView):
    template_name = 'news/form.html'
    form_class = forms.SimpleForm
    success_url = '/redirect/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer
    filterset_class = filters.NewsFilter


class NewsSumView(APIView):
    def get(self, request):
        count_of_news = models.News.objects.count()
        return Response({'news_count': count_of_news})
