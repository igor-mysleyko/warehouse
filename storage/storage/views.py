from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>info</h1>')

def all_goods(request):
    return HttpResponse('all goods')