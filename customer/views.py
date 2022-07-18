from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import CustomerLoginForm , CustomerRegistrationForm
from django.contrib.auth import get_user_model
from .models import Customer
from ecommerce.models import SellWaste
import reportlab
from reportlab.pdfgen import canvas

User = get_user_model()

# Create your views here.
def customer_login_view(request , backend='django.contrib.auth.backends.ModelBackend'):
    print('Customer Login View')
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('customer_login'))
    else:
        form = CustomerLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['customername']
            password = form.cleaned_data['customerpassword']
            user = authenticate(username=username,password=password)
            if user.is_customer or user.is_superuser:
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request,'Successfully Logged In')
                return HttpResponseRedirect(reverse('customer',args=[request.user]))
            else:
                messages.error(request,'Invalid Username Or Password')
                return HttpResponseRedirect(reverse('customer_login'))
        context = {
            'form':form,
            'login':True,
        }
        return render(request,'customer/form.html',context)

def customer_registration_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('customer_signin'))
    else:
        # print('yes')
        form = CustomerRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_customer = True
            new_user.save()
            login(request,new_user,backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Successfully Registered Customer Account. Please Enter the following details")
            return HttpResponseRedirect(reverse('customer_details'))

        context = {
            "form":form,
            "signin":True,
        }
        return render(request, "customer/form.html", context)

def customer_view(request,user):
    if not request.user.is_authenticated:
        messages.error(request,'You are logged out or not authenticated')
        return HttpResponseRedirect(reverse('customer_login'))
    else:
        context = {}
        return render(request,"customer/customer.html",context)

def customer_details_view(request):
    if request.method == 'POST':
        new_customer = Customer.objects.create(user = request.user)
        new_customer.first_name = request.POST.get('first_name')
        new_customer.last_name = request.POST.get('last_name')
        new_customer.middle_name = request.POST.get('middle_name')
        new_customer.phone_number = request.POST.get('phone_number')
        new_customer.save()
        return HttpResponseRedirect(reverse('customer',args=[request.user]))
    context = {}
    return render(request,'customer/form.html',context)

def buy_view(request):
    items = SellWaste.objects.filter(active=True)
    context = {
        'items' : items,
    }
    return render(request,'customer/sell_waste.html',context)

def add_drop_location_view(request,id):
    if request.method == "POST":
        item = SellWaste.objects.get(id=id)
        item.drop_address = request.POST.get('drop_address')
        item.save()
        return HttpResponseRedirect(reverse('checkout',args=[id]))
    
    context = {
        'drop_address' : True,
        'id' : id,
    }
    return render(request,'customer/form.html',context)