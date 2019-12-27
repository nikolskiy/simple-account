from collections import OrderedDict
from time import time
from decimal import Decimal
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Customer
from .serializers import CustomerSerializer, UpdateSerializer, InfoSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """Manage customer records"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AccountMixin:
    serializer_class = UpdateSerializer
    customer_serializer_class = CustomerSerializer

    def transaction(self, obj, data, resp):
        resp['status'] = status.HTTP_200_OK
        resp['result'] = True
        customer_serializer = self.customer_serializer_class(instance=obj)
        resp['addition'] = customer_serializer.data
        return Response(resp, status=resp['status'])

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return self.build_response(serializer)

    def build_response(self, serializer):
        resp = OrderedDict([
            # If this was not replaced something went wrong.
            ('status', status.HTTP_500_INTERNAL_SERVER_ERROR),
            ('result', False),
            ('addition', {}),
            ('description', {})
        ])

        # make sure we got valid request from the user
        if not serializer.is_valid():
            resp['status'] = status.HTTP_400_BAD_REQUEST
            resp['addition'] = {}
            resp['description'] = {'errors': serializer.errors}
            return Response(resp, status=resp['status'])
        obj = Customer.objects.filter(uuid=serializer.data['uuid']).first()
        if not obj:
            resp['status'] = status.HTTP_400_BAD_REQUEST
            resp['addition'] = {}
            resp['description'] = [
                'Customer with {} uuid does not exist.'.format(
                    serializer.data['uuid']
                )
            ]
            return Response(resp, status=resp['status'])

        return self.transaction(obj, serializer.data, resp)


class AddView(AccountMixin, generics.GenericAPIView):
    """Increase balance"""

    def transaction(self, instance, data, resp):
        amount = Decimal(data['amount'])
        instance.balance += amount
        instance.save()
        resp['status'] = status.HTTP_200_OK
        resp['result'] = True
        resp['addition'] = self.customer_serializer_class(instance=instance).data
        return Response(resp, status=resp['status'])


class SubtractView(AccountMixin, generics.GenericAPIView):
    """Place a hold"""

    def transaction(self, instance, data, resp):
        amount = Decimal(data['amount'])
        if instance.balance - instance.hold - amount < 0:
            resp['status'] = status.HTTP_400_BAD_REQUEST
            resp['result'] = False
            resp['addition'] = self.customer_serializer_class(instance=instance).data
            resp['description'] = {
                'errors': ['Not enough funds']
            }
            return Response(resp, status=resp['status'])

        instance.hold += amount
        instance.save()

        resp['status'] = status.HTTP_200_OK
        resp['result'] = True
        resp['addition'] = self.customer_serializer_class(instance=instance).data
        return Response(resp, status=resp['status'])


class StatusView(AccountMixin, generics.GenericAPIView):
    """Balance Status"""

    serializer_class = InfoSerializer


@api_view()
def ping(request):
    data = OrderedDict([
        ('status', status.HTTP_200_OK),
        ('result', True),
        ('addition', {'operation': 'ping'}),
        ('description', {})
    ])
    return Response(data, status=data['status'])


@api_view()
def rebalance(request):
    updated = []
    t0 = time()
    for customer in Customer.objects.filter(hold__gt=0):
        customer.balance -= customer.hold
        customer.hold = 0
        customer.save()
    delta = time() - t0
    msg = '{} customers rebalanced in {} seconds.'.format(len(updated), delta)
    return Response(msg, status=status.HTTP_200_OK)


add_view = AddView.as_view()
subtract_view = SubtractView.as_view()
status_view = StatusView.as_view()
