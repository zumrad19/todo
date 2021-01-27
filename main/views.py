from django.shortcuts import render, HttpResponse


def homepage(request):
    return HttpResponse("Hello world")


def test(request):
    return HttpResponse("test")


def second(request):
    return HttpResponse("second")


def third(request):
    return HttpResponse("third")
