from django.urls import path
from rental import views

urlpatterns = [
    path('home/', views.cur_dateplustime),
]