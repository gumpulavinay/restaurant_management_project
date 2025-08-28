
from django.shortcuts import render 
from .models import Restaurant

def homepage(request):
    restaurant = Restaurant.objects.first()
    return render (request,'homepage.html, {"phone_number": restaurant.phone}')