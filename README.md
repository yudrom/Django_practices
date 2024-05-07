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

In [18]: 
Out[18]:

In [19]: 
Out[19]:

In [20]: 
Out[20]:

In [21]: 
Out[21]:

In [22]: 
Out[22]:

In [23]:
Out[23]:

In [24]:
Out[24]:

In [25]:
Out[25]:






