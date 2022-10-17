from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.
def get_product(request, product_id):
    product=Product.objects.get (id= product_id)
    context={
        "product":{
            "id":product_id,
            "name":product.name,
            "description":product.description,
            "price":product.price }
        }
    
    return render (request, "product_detail.html", context)
    #return HttpResponse(f""" <p>{product.id} </p>
     #<p1>{product.name}</p1> 
     #<p1>{product.price}</p>
     #""")
     #three quatations for multiple lines 
    
def get_products(request):
    products=Product.objects.all()
    list_products=[]
    for product in products:
        list_products.append({"name":product.name,  "price":product.price})

    context={"products":list_products }
    return render (request, "product-list.html",context)


def get_home(request):
    return HttpResponse ("Welcome to Online Store")