from django.utils.crypto import get_random_string
from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Delete users"

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='User ID')

    def handle(self, *args, **options):
        user_ids = options['user_id']
        for user_id in user_ids:
            try:
                user= User.objects.get(pk=user_id)
                user.delete()
                self.stdout.write(self.style.SUCCESS(f"Successfully {user.username} has been deleted."))
            except User.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"{user.username} is not exist."))