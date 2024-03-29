import random

from django.db import transaction
from django.core.management.base import BaseCommand

from archive.models import Person, Interview
from archive.factories import PersonFactory

NUM_PEOPLE = 50

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        #self.stdout.write("Deleting old data...")
        #models = [Person]
        #for m in models:
        #    m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the people
        people = []
        for _ in range(NUM_PEOPLE):
            person = PersonFactory()
            people.append(person)
