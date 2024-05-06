from django.db import models
from datetime import date


class Car(models.Model):

    FUEL_TYPE_CHOICES = (
        ('gasoline', 'Бензин'),
        ('diesel', 'Дизель'),
        ('electricity', 'Электричество'),
        ('other', 'Другое')
    )

    name = models.CharField('Марка', max_length=100)
    release_date = models.DateField('Дата изготовления', default=date.today)
    color = models.CharField('Цвет', max_length=100, blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0)
    fuel_type = models.CharField('Тип топлива', choices=FUEL_TYPE_CHOICES, default='gasoline', max_length=100)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self) -> str:
        return self.name


class RentalAgency(models.Model):

    SERVICES_CHOICES = (
        ('daily_rental', 'Ежедневная аренда'),
        ('hourly_rental', 'Почасовая аренда'),
        ('additional_services', 'Дополнительные услуги')
    )

    name = models.CharField('Название агентства', max_length=100)
    address = models.CharField('Адрес', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=20)
    logo = models.ImageField('Логотип', upload_to='pictures', null=True, blank=True)
    services = models.CharField('Услуга', choices=SERVICES_CHOICES, default='daily_rental', max_length=100)

    class Meta:
        verbose_name = 'Агентство аренды'
        verbose_name_plural = 'Агентства аренды'

    def __str__(self):
        return self.name
