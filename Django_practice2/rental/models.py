from django.db import models


class Car(models.Model):
    name = models.CharField('Марка', max_length=100)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self) -> str:
        return self.name


class RentalAgency(models.Model):
    name = models.CharField('Название агентства', max_length=100)
    address = models.CharField('Адрес', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=20)

    class Meta:
        verbose_name = 'Агентство аренды'
        verbose_name_plural = 'Агентства аренды'

    def __str__(self):
        return self.name
