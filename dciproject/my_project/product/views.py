from django.shortcuts import render

from rest_framework import generics
from .serializers import ProductSerializer
from product.models import Product



# Create your views here.
class ProductList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
     queryset = Product.objects.all()
     serializer_class = ProductSerializer

class ProductUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def index(request): #THIS IS THE UPDATED VERSION USING MTV paradigm
    return render(request,'product/index.html')