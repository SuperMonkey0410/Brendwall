from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def index(request):
    return render(request, 'api/index.html')