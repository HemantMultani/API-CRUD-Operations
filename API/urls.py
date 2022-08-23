from django.urls import path
from . import views

urlpatterns = [
    path('drinks', views.drink_list, name='drink_list'),
    path('drinks/<str:id>', views.drink_details, name='drink_details'),
]