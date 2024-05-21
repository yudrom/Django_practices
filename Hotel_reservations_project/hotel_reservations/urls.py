from django.urls import path
from hotel_reservations import views


urlpatterns = [
    path('', views.index, name='main'),
]

