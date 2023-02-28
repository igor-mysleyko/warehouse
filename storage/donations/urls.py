
from django.urls import path
from .views import index, all_goods, customer, category




urlpatterns = [

    path('index/',index, name='home'),
    path('all_goods/',all_goods, name='all_goods'),
    path('customer/', customer, name='customer'),
    path('category/', category, name='category'),

]