# Generated by Django 5.0.4 on 2024-05-07 00:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_rentalagency'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, max_length=100, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('gasoline', 'Бензин'), ('diesel', 'Дизель'), ('electricity', 'Электричество'), ('other', 'Другое')], default='gasoline', max_length=100, verbose_name='Тип топлива'),
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='car',
            name='release_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата изготовления'),
        ),
        migrations.AddField(
            model_name='rentalagency',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='Логотип'),
        ),
        migrations.AddField(
            model_name='rentalagency',
            name='services',
            field=models.CharField(choices=[('daily_rental', 'Ежедневная аренда'), ('hourly_rental', 'Почасовая аренда'), ('additional_services', 'Дополнительные услуги')], default='daily_rental', max_length=100, verbose_name='Услуга'),
        ),
    ]
