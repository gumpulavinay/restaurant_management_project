from django.shortcuts import render

# Create your views here.
def contact_us(request):
    contact_info = {
        "email":"support@example.com",
        "phone": "+91 98765 43210",
        "address": "123, Main Street,Hyderabad,India"
    }
    return render(request,"contact_us.html",{"contact":contact_info})