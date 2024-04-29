# Generated by Django 5.0.4 on 2024-04-29 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalAgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название агентства')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Агентство аренды',
                'verbose_name_plural': 'Агентства аренды',
            },
        ),
    ]
