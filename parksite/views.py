from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return render(request, "index.html")


def charts(request):
    return render(request, "charts.html")


def ls(request):
    return render(request, "layout-static.html")


def index(req):
    context = {

    }

    return render(req, "index.html", context=context)
