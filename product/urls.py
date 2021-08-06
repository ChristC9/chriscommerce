from django.urls import path
from .views import *


urlpatterns=[
    path('',products,name="all-products"),
    path('cartview/<str:orderStr>',cartView,name="cart-view"),
    path('checkout/<str:orderStr>',checkout,name="check-out"),
    path('orders/',myOrder,name="my-orders")
]