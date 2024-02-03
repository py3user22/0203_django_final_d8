from django.shortcuts import render
from .models import Menu
from django.core import serializers
from datetime import datetime
import json
from .forms import BookingForm
from .models import Booking


# Create your views here.
def home1(request):
    return render(request, '0203_django_notes2.html', {})

#0203 menu method add.
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def about(request):
    return render(request, 'about.html', {})

def home(request):
    return render(request, 'index.html',{})

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)


# def bookings(request):