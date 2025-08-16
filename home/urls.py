from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),  # homepage
    path('restaurant/', restaurant_page, name='restaurant_page'),
]