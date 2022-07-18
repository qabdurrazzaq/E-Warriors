
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth.decorators import login_required

from customer.models import Customer
from .models import SellWaste
import stripe
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

try:
    stripe_pub = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret = settings.STRIPE_SECRET_KEY
except Exception as e:
    print(str(e))
    raise NotImplementedError(str(e))

stripe.api_key = stripe_secret

@login_required
def checkout_view(request,id):
    try:
        item = SellWaste.objects.get(id=id)
    except:
        item.id = None
        return HttpResponseRedirect(reverse('view_waste'))
    if request.method == 'POST':
        try:
            user_stripe = request.user.userstripe.stripe_id
            customer = stripe.Customer.retrieve(user_stripe)
        except:
            customer = None
            pass
        user = Customer.objects.get(user=request.user)
        token = request.POST['stripeToken']
        charge = stripe.Charge.create(
            amount = int(item.price*100),
            currency = 'inr',
            description = "Charge for %s to E-Warriors. Full name of the Customer: %s %s %s. Customer Mobile Number %s. Item Name: %s. Item Price: %s. Item Drop Location: %s" %(user,user.first_name,user.middle_name,user.last_name,user.phone_number,item.title,item.price,item.drop_address),
            source = 'tok_visa',
        )
        print(charge)
        if charge['captured']:
            item.active = False
            item.save()
            messages.success(request, "Your Items has been purchased refer <a href='https://dashboard.stripe.com/test/payments'> https://dashboard.stripe.com/test/payments </a>",extra_tags='safe')
            return HttpResponseRedirect(reverse('home'))
    context = {
        'item' : item,
        'stripe_pub' : stripe_pub,
    }
    return render(request,'Ewarriors/checkout.html',context)
