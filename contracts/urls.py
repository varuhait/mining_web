from django.contrib import admin
from django.urls import include, path
from contracts import views

urlpatterns = [
    path('', views.contracts, name='contracts' ),
    path('contracts_result', views.contracts_result, name='contracts_result')
]
