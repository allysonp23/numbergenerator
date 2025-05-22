from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


class Command(BaseCommand):
    help = 'Generate JWT access and refresh tokens for a given user'

    def add_arguments(self, parser):
        parser.add_argument(
            'username',
            type=str,
            help='Username to generate tokens for'
        )

    def handle(self, *args, **options):
        User = get_user_model()
        username = options['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError(f'User "{username}" does not exist')
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        self.stdout.write(f'Refresh token: {str(refresh)}')
        self.stdout.write(f'Access token: {str(access)}')
