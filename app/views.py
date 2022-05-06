from django.shortcuts import render
from rest_framework.response import Response
from .models import product
from .serializers import productSerializer
from rest_framework import status
from rest_framework.views import APIView


#Create your views here.


#get/search
class productAPI(APIView):
  def get (self, request, pk=None, format=None):
    id = pk
    if id is not None:
      pro = product.objects.get(id=id)
      serializer = productSerializer(pro)
      return Response(serializer.data)
    
    pro = product.objects.all()
    serializer = productSerializer(pro, many=True)
    return Response(serializer.data)


  #post/add/create
  def post(self, request, format=None):
    serializer = productSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'DATA Created'}, status=status.HTTP_201_CREATED)
    return Response({'msg':'BAD TYPE OF REQUEST'}, status=status.HTTP_400_BAD_REQUEST)


  #put/update
  def put(self, request, pk, format=None):
    id = pk
    pro = product.objects.get(pk=id)
    serializer = productSerializer(pro, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'DATA UPDATED'}, status=status.HTTP_200_OK)
    return Response({'msg':'BAD TYPE OF REQUEST'}, status=status.HTTP_400_BAD_REQUEST)



  #patch/partial_update
  def patch(self, request, pk, format=None):
    id = pk 
    pro = product.objects.get(pk=id)
    serializer = productSerializer(pro, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Partial DATA UPDATED'}, status=status.HTTP_200_OK)
    return Response({'msg':'BAD TYPE OF REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
  

  #delete
  def delete(self, request, pk, format=None):
    id = pk
    pro = product.objects.get(pk=id)
    serializer = productSerializer(pro, data=request.data, partial=True)
    if serializer.is_valid():
      pro.delete()
      return Response({'msg':'SUCCESS'}, status=status.HTTP_200_OK)
    return Response({'msg':'BAD TYPE OF REQUEST'}, status=status.HTTP_400_BAD_REQUEST)