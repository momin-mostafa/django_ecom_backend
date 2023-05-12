# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

    
@api_view(['GET'])
def getall(request):
    api_urls = {
		'List':'/product-list/',
		'Detail View':'/product/<str:pk>/',
		'Create':'/product-list/',
		'Update':'comming soon',
		'Delete':'/product/<str:pk>/',
		}
    return Response(api_urls)

@api_view(['GET','POST'])
def products(request):
    if request.method == "GET":
        product = Product.objects.all()
        serializer = ProductSerializer(product,many = True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.error_messages)
        serializer.save()    
        return Response("Successfully Added")
    return Response('product')


@api_view(['GET','DELETE','PUT'])
def product(request,pk):
    if request.method == "GET":
        product = Product.objects.filter(pk = pk)
        serializer = ProductSerializer(product,many = True)
        return Response(serializer.data)
    if request.method == "DELETE":
        Product.objects.filter(pk = pk).delete()
        return Response(f"DELETE CALLED on Product {pk}")
    if request.method == "PUT":
        # product = Product.objects.filter(pk = pk)
        # serializer = ProductSerializer(data = request.data)
        # if not serializer.is_valid():
        #     return Response(serializer.error_messages)
        # product.values = serializer.
        return Response(f"Put Called on product {pk}. Comming soon")
    return Response('product')

