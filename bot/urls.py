from django.urls import path
from . import views


app_name = 'bot'

urlpatterns = [
    path('', views.home_page, name='home_page'),
]
