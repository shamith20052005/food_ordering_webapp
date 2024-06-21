from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.views import APIView
from orders.models import Orders, Address
from .forms import AddressForm


# Create your views here.

@login_required
def user_orders(request):
  orders = Orders.objects.filter(user=request.user).order_by('-date')  

  for order in orders:
    order.total_price = order.get_total_price()  

  context = {'orders': orders}
  return render(request, 'orders/user_orders.html', context)


@login_required
def add_address_in_order_create(request):
  if request.method == 'POST':
    form = AddressForm(request.POST, request=request)
    if form.is_valid():
      address = form.save(commit=False)
      address.user = request.user
      address.save()
      return redirect('create_order')  
  else:
    form = AddressForm(request=request)

  context = {'address_form': form}

  return render(request, 'orders/address_form.html', context)

