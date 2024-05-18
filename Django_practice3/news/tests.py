from django.test import TestCase
from django.test import Client
from news import models


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
