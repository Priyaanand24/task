from django.http import request
from django.shortcuts import render
from rest_framework import generics
from ..models import *
from ..serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    """
    sample testing for token generation
    username : priya
    password : admin
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class AccountViewSet(ModelViewSet):
    """
    viewset for CRUD Account
    """
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer


class StoreViewSet(ModelViewSet):
    """
    viewset for CRUD Store
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (IsAuthenticated,)


class ProductViewSet(ModelViewSet):
    """
    viewset for CRUD Store
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class CustomersViewSet(ModelViewSet):
    """
    viewset for CRUD Store
    """
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    permission_classes = (IsAuthenticated,)
