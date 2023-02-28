from django.shortcuts import render
from django.http import HttpResponse


goods = [
    {'name' : 'phone', 'coast' : 2000},
    {'name' : 'tv', 'coast' : 5000},
    {'name' : 'PC', 'coast' : 4000},
    {'name' : 'notebook', 'coast' : 3500},
    {'name' : 'PS5', 'coast' : 3800},
]

def index(request):
    return render(request,'index.html',)

def all_goods(request):
    return render(request,'all_goods.html',{'goods': goods})

def customer(request):
    return render(request, 'customer.html')

def category(request):
    return render(request,'category.html')