from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


def mypassaction(request):
    return render(request, "registration/password_reset_done.html")
