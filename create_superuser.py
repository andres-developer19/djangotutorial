import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from django.contrib.auth.models import User

username = "admin"
password = "admin"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, "andres@example.com", password)
    print("✅ Superusuario creado correctamente.")
else:
    print("⚠️ El superusuario ya existe.")
