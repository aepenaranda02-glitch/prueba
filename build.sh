#!/usr/bin/env bash
# ============================================================
# build.sh — Render lo ejecuta en cada deploy
# ============================================================
set -o errexit

echo "📦 Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

echo "📁 Recolectando estáticos..."
python manage.py collectstatic --noinput

echo "🗄️ Aplicando migraciones..."
python manage.py migrate --noinput

echo "👤 Creando superusuario si no existe..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
import os
U = get_user_model()
username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
if username and password and not U.objects.filter(username=username).exists():
    U.objects.create_superuser(
        username=username,
        email=os.environ.get("DJANGO_SUPERUSER_EMAIL", ""),
        password=password,
    )
    print("Superusuario creado:", username)
else:
    print("Sin cambios en superusuario.")
EOF

echo "✅ Build completado"