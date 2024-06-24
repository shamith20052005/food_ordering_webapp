from rest_framework import serializers
from django.contrib.auth.models import User
from home.models import Menu, Category
from orders.models import Orders, Address
from cart.models import Cart, CartItem
from django.contrib.auth import authenticate

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

# authentication

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Fields you want to expose

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Don't include password in response

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user