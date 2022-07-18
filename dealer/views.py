from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import DealerLoginForm , DealerRegistrationForm
from django.conf import settings
from django.contrib.auth import get_user_model
from ecommerce.models import SellWaste
from .models import Dealer

User = get_user_model()

# Create your views here.
def dealer_login_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('dealer_login'))
    else:
        form = DealerLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['dealername']
            password = form.cleaned_data['dealerpassword']
            user = authenticate(username=username,password=password)
            if user.is_dealer or user.is_superuser:
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request,'Successfully Logged In')
                return HttpResponseRedirect(reverse('dealer',args=[request.user]))
            else:
                messages.error(request,'Invalid Username Or Password')
                return HttpResponseRedirect(reverse('dealer_login'))
        context = {
            'form':form,
            'login':True,
        }
        return render(request,'dealer/form.html',context)

def dealer_registration_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('dealer_register'))
    else:
        form = DealerRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_dealer = True
            new_user.save()
            login(request,new_user,backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Successfully Registered Dealer Account. Please Enter the following details")
            return HttpResponseRedirect(reverse('dealer_details'))

        context = {
            "form":form,
            "signin":True,
        }
        return render(request, "dealer/form.html", context)

def dealer_view(request,user):
    if not request.user.is_authenticated:
        messages.error(request,'You are logged out or not authenticated')
        return HttpResponseRedirect(reverse('dealer_login'))
    else:
        context = {}
        return render(request,"dealer/dealer.html",context)

def dealer_details_view(request):
    if request.method == 'POST':
        new_dealer = Dealer.objects.create(user = request.user)
        new_dealer.first_name = request.POST.get('first_name')
        new_dealer.last_name = request.POST.get('last_name')
        new_dealer.middle_name = request.POST.get('middle_name')
        new_dealer.phone_number = request.POST.get('phone_number')
        new_dealer.stripe_pub_api = request.POST.get('stripe_pub_api')
        new_dealer.stripe_secret_api = request.POST.get('stripe_secret_api')
        new_dealer.save()
        return HttpResponseRedirect(reverse('dealer',args=[request.user]))
    context = {}
    return render(request,'dealer/form.html',context)

def add_waste_view(request):
    if request.method == 'POST':
        item = SellWaste.objects.create()
        item.title = request.POST.get('title')
        item.description = request.POST.get('description')
        item.price = request.POST.get('price')
        item.pickup_address = request.POST.get('pickup_address')
        item.active = True
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('home'))
    context = {
        'add_item' : True,
    }
    return render(request,'dealer/form.html',context)

def view_waste_view(request):
    items = SellWaste.objects.filter(user=request.user).filter(is_admins=False)
    print(items)
    context = {
        'items' : items
    }
    return render(request,'dealer/view_waste.html',context)

def remove_item_view(request,id):
    print('yes')
    try:
        item = SellWaste.objects.get(id=id)
    except:
        return HttpResponseRedirect(reverse('view_waste'))
    item.delete()
    return HttpResponseRedirect(reverse('view_waste'))

