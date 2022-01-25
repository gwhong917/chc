from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Test

from django.db import connection


# def index(request):
#     return render(request, "index.html")

def test2(request):
    return render(request, "test2.html")


def test(request):
    #CASE1 :
    testChart = Test.objects.all()
    print(type(testChart))

    jacob_test = Test.objects
    jacob_test_bold = jacob_test.filter(t_job='bold').count()
    jacob_test_progay = jacob_test.filter(t_job='progay').count()
    jacob_test_programmer = jacob_test.filter(t_job='programmer').count()
    jacob_test_smoker = jacob_test.filter(t_job='smoker').count()
    pie_chart_test = [jacob_test_bold, jacob_test_progay, jacob_test_programmer, jacob_test_smoker]
    print(type(pie_chart_test))

    return render(request, "test.html", {
        'pie_chart_test': pie_chart_test,
        'testChart': testChart,

    })


def charts_4(request):

    jacob_test = Test.objects
    jacob_test_bold = jacob_test.filter(t_job='bold').count()
    jacob_test_progay = jacob_test.filter(t_job='progay').count()
    jacob_test_programmer = jacob_test.filter(t_job='programmer').count()
    jacob_test_smoker = jacob_test.filter(t_job='smoker').count()

    pie_chart_test = [jacob_test_bold, jacob_test_progay, jacob_test_programmer, jacob_test_smoker]
    print(type(pie_chart_test))

    return render(request, "charts_4.html", {
        'pie_chart_test': pie_chart_test,
    })


def tables_time2(request):

    data_table_test = Test.objects.all()
    print(type(data_table_test))

    return render(request, "tables_time2.html", {
        'data_table_test': data_table_test
    })


def index(request):
    return render(request, "index.html")


def charts(request):
    return render(request, "charts.html")


def ls(request):
    return render(request, "layout-static.html")


def lsl(request):
    return render(request, "layout-sidenav-light.html")


def h401(request):
    return render(request, "401.html")


def h404(request):
    return render(request, "404.html")


def h500(request):
    return render(request, "500.html")


def login(request):
    return render(request, "login.html")


def password(request):
    return render(request, "password.html")


def register(request):
    return render(request, "register.html")


def tables(request):
    return render(request, "tables.html")


def charts_1(request):
    return render(request, "charts_1.html")


def charts_2(request):
    return render(request, "charts_2.html")


def charts_3(request):
    return render(request, "charts_3.html")


def tables_area1(request):
    return render(request, "tables_area1.html")


def tables_area2(request):
    return render(request, "tables_area2.html")


def tables_time1(request):
    return render(request, "tables_time1.html")







