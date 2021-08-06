from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Product,OrderItem,Order
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def products(request):
    return render(request,'product/index.html',{'title':"All Products",'Products':Product.objects.all()})



def cartView(request,orderStr):
    order=orderStr.split(',')
    orderList=Product.objects.filter(pk__in=order).values('id','name','image','price')
    order_list=json.dumps(list(orderList),cls=DjangoJSONEncoder)
    return render(request,'product/cartview.html',{'title':"Cart_Items",'Orders':order_list})
    
@login_required
def checkout(request,orderStr):
    order = saveOrder(request,orderStr)
    saveItems(request,order,orderStr)
    messages.success(request,f'Orders Added Successfully!')
    return redirect('/')

def saveOrder(request,orderStr):
    orderList=orderStr.split(',')
    total=0
    for order in orderList:
        orderId=order.split(':')[0]
        orderQty=order.split(':')[1]
        product=Product.objects.get(pk=orderId)
        total+=product.price * int(orderQty)
    orders=Order()
    orders.count=len(orderList)
    orders.total=total
    orders.userId=request.user
    orders.save()
    return orders    


def saveItems(request,orders,orderStr):
    orderList=orderStr.split(',')
    total=0
    for order in orderList:
        orderId=order.split(':')[0]
        orderQty=order.split(':')[1]
        product=Product.objects.get(pk=orderId)
        total+=product.price *int(orderQty)
        
        orderItems=OrderItem()
        orderItems.name=product.name
        orderItems.price=product.price
        orderItems.image=product.image
        orderItems.count=int(orderQty)
        orderItems.orderId=orders
        orderItems.userId=request.user
        
        orderItems.save()
    
    

def myOrder(request):
    user=request.user
    orders=Order.objects.filter(userId=user)
    order=[]
    for o in orders:
        order.append({'order':o,'orderitem':o.items.all()})
    return render(request,'product/myorders.html',{'title':'My Orders', 'orders':order})