from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **options):
        print(options, "Javed ----------->", args)
        try:
            User.objects.get(username="umar")
        except User.DoesNotExist:
            User.objects.create_superuser('umar', 'umar@gmail.com', 'pass')
            raise CommandError('User "%s" does not exist')