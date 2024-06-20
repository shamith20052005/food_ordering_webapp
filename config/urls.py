"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import SignupView
from home.views import Index, remove_from_cart_from_home, search_menu, add_to_cart_from_search
from orders.views import user_orders, add_address_in_order_create
from cart.views import cart_view, add_to_cart, remove_from_cart, OrderCreateView, order_placed

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Index.as_view(), name='home'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/signup/", SignupView.as_view(), name='signup'),
    path("orders/", user_orders, name='user_orders'),
    path('cart/add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/remove-from-cart-from-home/<int:cart_item_id>/', remove_from_cart_from_home, name='remove_from_cart'),
    path('cart/create-order/', OrderCreateView.as_view(), name='create_order'),
    path('cart/order-placed/<int:pk>', order_placed, name='order_placed'),
    path('cart/add-address/', add_address_in_order_create, name='add_address'),
    path('cart/', cart_view, name='cart_view'),
    path('search/', search_menu, name='search_menu'),
    path('search/add-to-cart/<int:item_id>/', add_to_cart_from_search, name='add_to_cart_search'),

    path('api/', include('api.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
