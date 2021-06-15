from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "website/index.html")


def samples(request):
    return render(request, "website/samples.html")


def temp_twilio(request):
    return HttpResponse(request)
