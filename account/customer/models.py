from uuid import uuid4
from django.db import models


class Customer(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=500)

    # values up to 999999.99
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    hold = models.DecimalField(max_digits=8, decimal_places=2)

    status = models.BooleanField()
