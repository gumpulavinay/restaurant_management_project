
from django.shortcuts import render 

def homepage(request):
    context = {
        "restaurant_name": "Foodie Paradise","welcome_message": "welcome to Foodie Paradise! Enjoy our delicious menu and freat service." 
    }
    
    return render (request,'homepage.html',context)