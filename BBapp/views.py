import re

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Contact, Inquiry, Property
from django.contrib.auth.views import LoginView
from django.contrib import messages
import random
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')

def property_list(request):
    properties = Property.objects.all()

    property_type = request.GET.get("property_type")
    location = request.GET.get("location")
    budget = request.GET.get("budget")

    if property_type:
        properties = properties.filter(property_type=property_type)

    if location:
        properties = properties.filter(location__icontains=location)

    if budget:
        properties = properties.filter(price__lte=budget)

    return render(request, 'property_list.html', {'properties': properties})

def property_detail(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'property_detail.html', {'property': property})

@login_required
def contact_owner(request,id):
    property = get_object_or_404(Property, id=id)
    owner = property.owner 
    return render(request,'contact_owner.html',{'owner': property.owner})


def contact_us(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        messages.success(request, "Message sent successfully!")
        return redirect('contact') 
    return render(request, 'contact.html')

def inquiry(request):
    if request.method == 'POST':
        Inquiry.objects.create(
            property_type=request.POST['property_type'],
            location=request.POST['location'],
            budget=request.POST['budget'],
            phone=request.POST['phone'],
            email=request.POST['email']
        )
        
    return render(request, 'inquiry.html')

class CustomLoginView(LoginView):
    template_name = "login.html"
    
from django.contrib import messages

def book_property(request, id=None):
    property = None
    if id:
        property = Property.objects.get(id=id)

    if request.method == "POST":
        # You can save booking here if needed

        # ✅ Show success popup
        messages.success(request, "Your booking is confirmed 🎉")

        return redirect("book_property_simple")  # or any page

    return render(request, 'book_property.html', {'property': property})


def location(request):
    return render(request,'location.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

import re

from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        if not all([name, phone, email, password, confirm]):
            messages.error(request, "Please fill in all fields ❌")
            return redirect("/login/")

        if password != confirm:
            messages.error(request, "Passwords do not match ❌")
            return redirect("/login/")

        if User.objects.filter(username=email).exists():
            messages.error(request, "User already exists ❌")
            return redirect("/login/")

        User.objects.create_user(username=email, email=email, password=password)

        # ✅ SUCCESS MESSAGE
        messages.success(request, "Account created successfully! 🎉")

        return redirect("/login/?success=1")

    return render(request, "registration/login.html")



from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("login_email")
        password = request.POST.get("login_password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("/property/")   # ✅ redirect to home (Rent/Stay page)

        else:
            return redirect("/login/?error=invalid")

    return render(request, "registration/login.html")


# CONTACT US VIEW WITH EMAIL SENDING


import urllib.parse

def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        # Save to DB
        Contact.objects.create(
            name=name,
            phone=phone,
            email=email,
            message=message
        )

        # ✅ Create WhatsApp message
        text = f"""
New Contact Message

Name: {name}
Phone: {phone}
Email: {email}

Message:
{message}
"""

        encoded_text = urllib.parse.quote(text)

        # ✅ Your WhatsApp number (with country code)
        whatsapp_url = f"https://wa.me/919848862269?text={encoded_text}"

        return redirect(whatsapp_url)

    return render(request, 'contact.html')