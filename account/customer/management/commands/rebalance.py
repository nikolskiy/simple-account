from time import time
from django.core.management.base import BaseCommand
from customer.models import Customer


class Command(BaseCommand):
    help = 'Apply holds to customer accounts.'

    def handle(self, *args, **options):
        updated = []
        t0 = time()
        for customer in Customer.objects.filter(hold__gt=0):
            customer.balance -= customer.hold
            customer.hold = 0
            customer.save()
            updated.append(customer.uuid)
        delta = time() - t0
        msg = '{} customers rebalanced in {} seconds.'.format(len(updated), delta)
        self.stdout.write(self.style.SUCCESS(msg))
