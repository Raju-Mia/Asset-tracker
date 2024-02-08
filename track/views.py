from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404
from .models import *
from .serializers import AddEmployeeSerializer,\
    AddAssetSerializer,DelegateToSerializer,\
    WhenGiveAndReturnSerializer,ConditionGiveAndReturnSerializer,WhenReturnSerializer




# ==========Adding & Fetching Employee==============
class AddEmployeeView(APIView):

    def get(self, request):
        snippets = Employee.objects.all()
        serializer = AddEmployeeSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AddEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ==========Adding & Fetching Asset==============
class AddAssetView(APIView):

    def get(self, request):
        asset = Asset.objects.all()
        serializer = AddAssetSerializer(asset,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AddAssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ==========Delegate one or more devices to employees==============
class DelegateToView(APIView):
   
    def get(self, request):
        asset = DelegateTo.objects.all()
        serializer = DelegateToSerializer(asset,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DelegateToSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ==========See when a Device was checked out and returned==============
class WhenGiveAndReturnView(APIView):
    
    def get_object(self, pk):
        '''get a single Object'''
        try:
            return GiveBack.objects.get(pk=pk)
        except GiveBack.DoesNotExist:
            raise Http404

    def get(self,request,pk):                      
        obj = self.get_object(pk)
        serializer = WhenGiveAndReturnSerializer(obj)
        return Response(serializer.data)



# ==========Give back assets returned==============
class WhenReturnView(APIView):
    def post(self, request):
        
        serializer = WhenReturnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ==========Assets Condition it was handed out and returned==============
class ConditionGiveAndReturnView(APIView):
   
    def get_object(self, pk):
        try:
            return GiveBack.objects.get(pk=pk)
        except GiveBack.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        condition = self.get_object(pk)
        serializer = ConditionGiveAndReturnSerializer(condition)
        return Response(serializer.data)