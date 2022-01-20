from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return render(request, "index.html")

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


def charts_4(request):
    return render(request, "charts_4.html")


def tables_area1(request):
    return render(request, "tables_area1.html")


def tables_area2(request):
    return render(request, "tables_area2.html")


def tables_time1(request):
    return render(request, "tables_time1.html")


def tables_time2(request):
    return render(request, "tables_time2.html")




