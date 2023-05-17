#new - whole script added by instructor
from rest_framework import serializers 
from .models import Customer
from product.serializers import ProductSerializer

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['pk', 'name', 'email', 'created']

