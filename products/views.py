from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.
def get_product(request, product_id):
    product=Product.objects.get (id= product_id)
    return HttpResponse(f""" <p>{product.id} </p>
     <p1>{product.name}</p1> 
     <p1>{product.price}</p>
     """)
     #three quatations for multiple lines 
    
def get_home(request):
    return HttpResponse ("Welcome to Online Store")