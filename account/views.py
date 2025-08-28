from django.shortcuts import render

# Create your views here.
def menu_items(request):
    items = [
        {"name": "pizza","price": 250},
        {"name":"Burger","price":120},
        {"name":"sandwich","price":100},
    ]
    return render (request, "menu_items.html",{"items":items})
