from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """Manage customer records"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
