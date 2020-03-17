from django.core.management.base import BaseCommand
from django.utils import timezone
import datetime
import random

class Command(BaseCommand):
    help = "Random Date Generation"

    def generate_date(self):
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(2017, 2019)
        return datetime.date(year, month, day)

    
    def handle(self, *args, **kwargs):
        random_date = self.generate_date()
        self.stdout.write(self.style.SUCCESS(f"Random Date: {random_date}."))
