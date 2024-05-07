# Query Sets

In [1]: models.Car.objects.all()
Out[1]: <QuerySet [<Car: BMW>, <Car: Toyota>, <Car: Nissan>, <Car: Tesla>]>

In [2]: models.Car.objects.first()
Out[2]: <Car: BMW>

In [3]: models.Car.objects.last()
Out[3]: <Car: Tesla>

In [4]: models.Car.objects.count()
Out[4]: 4

In [5]: models.Car.objects.order_by('name')
Out[5]: <QuerySet [<Car: BMW>, <Car: Nissan>, <Car: Tesla>, <Car: Toyota>]>

In [6]: models.Car.objects.order_by('-name')
Out[6]: <QuerySet [<Car: Toyota>, <Car: Tesla>, <Car: Nissan>, <Car: BMW>]>

In [7]: models.Car.objects.filter(name__contains='T')
Out[7]: <QuerySet [<Car: Toyota>, <Car: Tesla>]>

In [8]: models.Car.objects.filter(name__exact='Nissan')
Out[8]: <QuerySet [<Car: Nissan>]>

In [9]: models.RentalAgency.objects.get(id=1)
Out[9]: <RentalAgency: FastRentLowPrice>

In [10]: list(models.RentalAgency.objects.all())
Out[10]: 
[<RentalAgency: FastRentLowPrice>,
 <RentalAgency: 5MinutesToGo>,
 <RentalAgency: DeservedOne>]

 In [11]: models.Car.objects.filter(price__gt=9000000)
Out[11]: <QuerySet [<Car: Tesla>]>

In [12]: models.Car.objects.filter(price__lt=4550000)
Out[12]: <QuerySet [<Car: Toyota>, <Car: Nissan>]>

In [13]: models.Car.objects.filter(price__gte=4550000)
Out[13]: <QuerySet [<Car: BMW>, <Car: Tesla>]>

In [14]: models.RentalAgency.objects.latest('services')
Out[14]: <RentalAgency: DeservedOne>

In [15]: models.RentalAgency.objects.earliest('services')
Out[15]: <RentalAgency: FastRentLowPrice>

In [16]: models.RentalAgency.objects.filter(id=4).exists()
Out[16]: False

In [17]: models.Car.objects.create(name='Porsche', price=9100000)
Out[17]: <Car: Porsche>

In [18]: models.Car.objects.update(color='Чёрный')
Out[18]: 5

In [19]: models.Car.objects.filter(id__lt=3).update(color='Белый')
Out[19]: 2

In [20]: models.Car.objects.filter(name__exact='Nissan').delete()
Out[20]: (1, {'rental.Car': 1})

In [21]: models.Car.objects.dates('release_date', 'day')
Out[21]: <QuerySet [datetime.date(1999, 5, 1), datetime.date(2022, 3, 16), datetime.date(2024, 5, 7)]>

In [22]: models.Car.objects.dates('release_date', 'day').reverse()
Out[22]: <QuerySet [datetime.date(2024, 5, 7), datetime.date(2022, 3, 16), datetime.date(1999, 5, 1)]>

In [23]: models.RentalAgency.objects.values('name', 'services')
Out[23]: <QuerySet [{'name': 'FastRentLowPrice', 'services': 'daily_rental'}, {'name': '5MinutesToGo', 'ser
vices': 'daily_rental'}, {'name': 'DeservedOne', 'services': 'hourly_rental'}]>

In [24]: models.RentalAgency.objects.values_list('name', 'address')
Out[24]: <QuerySet [('FastRentLowPrice', 'ул. Пушкина 39'), ('5MinutesToGo', 'ул. Достоевского 37'), ('Dese
rvedOne', 'ул. Карла Маркса 12')]>

In [25]: models.Car.objects.values_list('price', flat=True)
Out[25]: <QuerySet [Decimal('4550000.00'), Decimal('3185000.00'), Decimal('11850000.00'), Decimal('9100000.
00')]>





