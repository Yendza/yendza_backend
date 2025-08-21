#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# dentro de manage.py, antes de executar main()
from django.contrib.auth import get_user_model
import os

User = get_user_model()

username = os.getenv("DJANGO_SUPERUSER_USERNAME", "Moises")
email = os.getenv("DJANGO_SUPERUSER_EMAIL", "moisesedson.manuel@gmail.com")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "Desportivo")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superusuário criado com sucesso!")


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yendza_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
