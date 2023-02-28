from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('<h1>info</h1>')

def all_goods(request):
    return HttpResponse('all goods')