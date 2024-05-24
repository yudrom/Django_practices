from django.test import TestCase
from django.test import Client
from django.urls import reverse
from news import models
from rest_framework.test import APITestCase
from .models import News
from datetime import datetime
from .serializers import NewsSerializer


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = models.Category.objects.create(
            title='Политика'
        )
        self.news = models.News.objects.create(
            title='Новость из политики',
            content='Lorem Ipsum is simply dummy text',
            category=self.category
        )

    def test_home(self):
        response = self.client.get('//')
        self.assertEquals(response.status_code, 200)

    def test_category(self):
        response = self.client.get(f'/category/{self.category.id}')
        self.assertEquals(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/redirect/')
        self.assertEquals(response.status_code, 302)

    def test_form(self):
        response = self.client.get('/form_example/')
        self.assertEquals(response.status_code, 200)


class NewsViewSetTest(APITestCase):

    def setUp(self):
        self.client = Client()
        self.news_1 = News.objects.create(
            title='Первая новость',
            content='Контент внутри первой новости',
            is_published=True
        )

        self.news_2 = News.objects.create(
            title='Вторая новость',
            content='Контент внутри второй новости',
            is_published=False,
            updated_at = datetime.now()
        )

    def test_list(self):
        url = reverse('news-list')
        response = self.client.get(url)
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, serializer.data)

    def test_detail(self):
        url = reverse('news-detail', kwargs={'pk: self.news_1.pk'})
        response = self.client.get(url)
        serializer = NewsSerializer(self.news_1)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, serializer.data)

    def test_create(self):
        url = reverse('news-list')
        data = {'title': 'Созданная ковость', 'content': 'Созданный контент'}
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.get(pk=response.data['id']).title, 'Созданная новость')

    def test_update(self):
        url = reverse('news-detail', kwargs={'pk': self.news_1.pk})
        data = {'title': 'Обновлённая новость', 'content': 'Обновлённый контент'}
        response = self.client.put(url, data, format='json')
        self.assertEquals(response.status_code, 200)
        self.news_1.refresh_from_db()
        self.assertEquals(self.news_1.title, 'Обновлённая новость')

    def test_partial_update(self):
        url = reverse('news-detail', kwargs={'pk': self.news_1.pk})
        data = {'title': 'Патч новости'}
        response = self.client.patch(url, data, format='json')
        self.assertEquals(response.status_code, 200)
        self.news_1.refresh_from_db()
        self.assertEquals(self.news_1.title, 'Патч новости')

    def test_delete(self):
        url = reverse('news-detail', kwargs={'pk': self.news_1.pk})
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 204)
        self.assertEquals(News.objects.count(), 1)

