from django.shortcuts import render
from .models import Port

def home(request):
    allports=Port.objects.all()
    return render(request, 'portapp/home_no.html',{'keyports':allports}) #change to portapp/home for original
