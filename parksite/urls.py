from django.urls import path, include
from . import views

app_name = 'parksite'

urlpatterns = [
    path('', views.index),
    path('charts', views.charts),
    path('layout-static', views.ls),
    # path('index/', views.index, name='index'),

]

