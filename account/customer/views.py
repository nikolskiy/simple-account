from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """Manage customer records"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AddView(views.APIView):
    def get(self, request, format=None):
        return Response()

    def post(self, request, format=None):
        return Response()


class SubtractView(views.APIView):
    def get(self, request, format=None):
        return Response()

    def post(self, request, format=None):
        return Response()


class StatusView(views.APIView):
    def get(self, request, format=None):
        return Response()

    def post(self, request, format=None):
        return Response()


@api_view()
def ping(request):
    return Response({"message": "pong"})


add_view = AddView.as_view()
subtract_view = SubtractView.as_view()
status_view = StatusView.as_view()
