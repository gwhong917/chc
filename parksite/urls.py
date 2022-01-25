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
    path('tables', views.tables),
    path('charts_1', views.charts_1),
    path('charts_2', views.charts_2),
    path('charts_3', views.charts_3),
    path('charts_4', views.charts_4),
    path('tables_area1', views.tables_area1),
    path('tables_area2', views.tables_area2),
    path('tables_time1', views.tables_time1),
    path('tables_time2', views.tables_time2),
    path('test', views.test),
    path('test2', views.test2),
]

