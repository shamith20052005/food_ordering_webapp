# track/views.py

from django.shortcuts import render
from orders.models import Orders
from django.contrib.auth.decorators import login_required
import json

# Fixed coordinates for places
PLACES_COORDINATES = {
    'kameng': (26.190469525851636, 91.70166519138878),
    'barak': (26.18932135854, 91.70192368422727),
    'umiam': (26.188701075550213, 91.70213765919556),
    'gaurang': (26.191518233878398, 91.70111458946964),
    'manas': (26.188856628045386, 91.70035879616769),
    'dihing': (26.187851009462968, 91.69997313925899),
    'brahmaputra': (26.187366802068198, 91.69996562044052),
    'disang': (26.186132659845455, 91.69701319181004),
    'kapili': (26.18849955006568, 91.69681611671176),
    'siang': (26.189570719627927, 91.69697081443235),
    'dhansiri': (26.19404082239976, 91.6989380755118),
    'siang': (26.189570719627927, 91.69697081443235),
    'subansri': (26.192839135102027, 91.69471596219856),
    
}

LOHIT_CANTEEN_COORDINATES = (26.189251226639367, 91.69811230619253)


@login_required
def track_order(request, order_id):
    order = Orders.objects.get(id=order_id, user=request.user)
    
    if not order.is_placed():
        return render(request, 'track/not_available.html')
    if not order.address:
        return render(request, 'track/no_address.html')
    
    user_place = order.address.address.lower()
    user_coordinates = PLACES_COORDINATES.get(user_place)
    
    if not user_coordinates:
        return render(request, 'track/no_coordinates.html')

    context = {
        'user_coordinates': json.dumps(user_coordinates),
        'lohit_coordinates': json.dumps(LOHIT_CANTEEN_COORDINATES)
    }
    return render(request, 'track/track.html', context)
