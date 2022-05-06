from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers


#serializers
class productSerializer(ModelSerializer): 
  class Meta:
    model = product   
    fields = ['id','name','category_name','descreption','buy_price','sell_price','quantity']