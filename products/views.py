from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.
def get_product(request, product_id):
    product=Product.objects.get (id= product_id)
    return HttpResponse(f"The product ordered is a <h1>{product}</h1> ")
def get_home(request):
    return HttpResponse ("Welcome to Online Store")