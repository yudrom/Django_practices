from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


def cur_dateplustime(request):
    outputting_text = 'Текущая дата и время: {}'.format(timezone.now())
    return HttpResponse(outputting_text)
