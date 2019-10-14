from django.contrib import admin
from django.urls import include, path
from calculater import views

urlpatterns = [
    path('', views.calculater, name='calculater' ),
    path('calculate_result', views.calculate_result, name='calculate_result'),
    path('list', views.ore_list, name='list'),
]
