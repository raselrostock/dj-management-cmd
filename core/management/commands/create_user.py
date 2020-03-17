from django.utils.crypto import get_random_string
from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Create random users"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help= 'The number of users to be created.')
        # Optional Arguments
        """
        The Optional arguments can be passed in any order.

        """
        parser.add_argument('-p', '--prefix', type=str, help='Define a username as prefix', )
        # Flag Arguments
        """
        The optional arguments are flags, which are used to handle boolean values.

        """
        parser.add_argument('-a', '--admin', action='store_true', help='Create admin account', )

    
    def handle(self, *args, **options):
        total = options['total']
        prefix = options['prefix']
        admin = options['admin']
        for i in range(total):
            if prefix:
                username = f'{prefix}_{get_random_string()}'
            else:
                username = get_random_string()

            if admin:
                User.objects.create_superuser(username=username, email='', password='123')
            else:
                User.objects.create_user(username=username, email='', password='123')
        self.stdout.write(self.style.SUCCESS(f"Successfully {total} user has been created."))
