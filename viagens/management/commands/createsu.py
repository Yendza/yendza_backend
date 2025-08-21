from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Cria superusuário se não existir (usado no deploy)"

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME", "Moises")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "moisesedson.manuel@gmail.com")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "Desportivo")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superusuário '{username}' criado!"))
        else:
            self.stdout.write(self.style.WARNING(f"Superusuário '{username}' já existe."))
