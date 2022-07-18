"""PBL_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , re_path
from django.conf.urls.static import static
from django.conf import settings
from EWarriors import views as eview
from customer import views as customerviews
from dealer import views as dealerviews
from ecommerce import views as ecommerceview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', eview.home, name = 'home'),
    
    path('logout', eview.logout_view , name='logout'),
    path('events', eview.events_view , name = 'events'),
    path('rate', eview.waste_rate_view , name = 'waste_rate'),

    re_path(r'^administrator/cart/$' , eview.admin_cart_view,name='admin_cart'),
    re_path(r'^administrator/cart/checkout/(?P<id>\d+)/$' , eview.admin_checkout_view,name='admin_checkout'),
    re_path(r'^customer/payments/checkout/(?P<id>\d+)/$' , ecommerceview.checkout_view,name='checkout'),

    path('customer/accounts/login/',customerviews.customer_login_view,name='customer_login'),
    path('customer/accounts/register/',customerviews.customer_registration_view,name='customer_signin'),
    re_path(r'^customer/(?P<user>\w+)/$',customerviews.customer_view,name='customer'),
    path('customer/personal/details/',customerviews.customer_details_view,name='customer_details'),
    path('customer/buy/waste',customerviews.buy_view,name='buy'),
    re_path(r'^customer/add/drop_location/(?P<id>\d+)/$' , customerviews.add_drop_location_view,name='add_drop_location'),
    # path('customer/add/drop_location',customerviews.add_drop_location_view,name='add_drop_location'),

    path('dealer/accounts/login/',dealerviews.dealer_login_view,name='dealer_login'),
    path('dealer/accounts/register/',dealerviews.dealer_registration_view,name='dealer_signin'),
    re_path(r'^dealer/(?P<user>\w+)/$',dealerviews.dealer_view,name='dealer'),
    path('dealer/personal/details/',dealerviews.dealer_details_view,name='dealer_details'),
    path('dealer/add_waste/add_new_item/',dealerviews.add_waste_view,name='add_waste'),
    path('dealer/view_waste/your_items/',dealerviews.view_waste_view,name='view_waste'),
    re_path(r'^dealer/remove/(?P<id>\d+)/$' , dealerviews.remove_item_view, name='remove_item'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

