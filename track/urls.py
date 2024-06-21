

from django.urls import path
from . import views

urlpatterns = [
    path('order/<int:order_id>/', views.track_order, name='track_order'),
]
