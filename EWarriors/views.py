from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from dealer.models import Dealer
from ecommerce.models import SellWaste
import stripe

# Create your views here.
def home(request):
    template = 'EWarriors/home.html'
    context = {}
    return render(request,template,context)

def logout_view(request):
    logout(request)
    messages.warning(request, "Successfully Logged Out.")
    return HttpResponseRedirect(reverse('home'))

def events_view(request):
    template = 'Ewarriors/events.html'
    context = {}
    return render(request,template,context)

def waste_rate_view(request):
    template = 'Ewarriors/waste_rate.html'
    context = {}
    return render(request,template,context)

def admin_cart_view(request):
    items = SellWaste.objects.filter(is_admins = False)
    context = {
        'items' : items
    }
    return render(request,"Ewarriors/admin_cart.html",context)

def admin_checkout_view(request,id):
    try:
        item = SellWaste.objects.get(id=id)
    except:
        item = None
        return HttpResponseRedirect(reverse('view_waste'))
    user = Dealer.objects.get(user=item.user)
    try:
        stripe_pub = user.stripe_pub_api
        stripe_secret = user.stripe_secret_api
    except:
        stripe_pub = None
        stripe_secret = None
    print(stripe_pub)
    print(stripe_secret)
    if request.method == 'POST':
        try:
            user_stripe = user.userstripe.stripe_id
            print(user_stripe)
            customer = stripe.Customer.retrieve(user_stripe)
        except:
            customer = None
            pass
        token = request.POST['stripeToken']
        charge = stripe.Charge.create(
            amount = int(item.price*100),
            currency = 'inr',
            description = "EWarriors Charge to %s paid sucessfully. Full Name of Seller: %s %s %s. Phone Number of Seller %s. Item Purchased: %s. Item Price: %s. Item's Pickup Location: %s" %(user,user.first_name,user.middle_name,user.last_name,user.phone_number,item.title,item.price,item.pickup_address),
            source = 'tok_visa',
        )
        print(charge)
        if charge['captured']:
            item.is_admins = True
            item.save()
            messages.success(request, "Items Purchased",extra_tags='safe')
            return HttpResponseRedirect(reverse('home'))
    context = {
        'item' : item,
        'stripe_pub' : stripe_pub,
    }
    return render(request,'Ewarriors/admin_checkout.html',context)
