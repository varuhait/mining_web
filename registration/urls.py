from django.urls import include, path
import registration.views as views
import registration.forms as forms

urlpatterns = [
    path('', views.signup, name='signup')
]
