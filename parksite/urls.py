from django.urls import path, include
from . import views

app_name = 'parksite'

urlpatterns = [
    path('', views.index),
    path('charts', views.charts),
    path('layout-static', views.ls),
    # path('index/', views.index, name='index'),
    path('layout-sidenav-light', views.lsl),
    path('401', views.h401),
    path('404', views.h404),
    path('500', views.h500),
    path('login', views.login),
    path('password', views.password),
    path('register', views.register),
    path('tables', views.tables)

]

