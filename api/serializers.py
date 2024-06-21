from rest_framework import serializers
from django.contrib.auth.models import User
from home.models import Menu, Category
from orders.models import Orders, Address
from cart.models import Cart, CartItem

# Home 

class MenuSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    class Meta:
        model = Menu
        fields = ['id', 'item', 'description', 'price', 'category', 'veg_or_nonveg', 'image', 'is_available']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']

# Orders 

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(many=True, slug_field='item', read_only=True)
    get_total_price = serializers.SerializerMethodField()

    def get_get_total_price(self, obj):
        return obj.get_total_price()

    class Meta:
        model = Orders
        fields = ['id', 'items', 'mode_of_eating', 'date', 'time', 'status', 'address', 'get_total_price']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'address']


# user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']  

# cart

class CartItemSerializer(serializers.ModelSerializer):
    menu_item = MenuSerializer(read_only=True)  

    class Meta:
        model = CartItem
        fields = ['id', 'menu_item', 'quantity']
         
        

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True, source='cart_items')  

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
        read_only_fields = ['user']


class TrackOrderSerializer(serializers.ModelSerializer):
    user_coordinates = serializers.SerializerMethodField()
    lohit_coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Orders
        fields = ['id', 'status', 'address', 'user_coordinates', 'lohit_coordinates']

    def get_user_coordinates(self, obj):
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
            'subansri': (26.192839135102027, 91.69471596219856),
        }
        address = obj.address.address.lower()
        return PLACES_COORDINATES.get(address)

    def get_lohit_coordinates(self, obj):
        return (26.189251226639367, 91.69811230619253)