#!/usr/bin/env bash
# build.sh — Script de construcción para Render

# Detiene el script si hay un error
set -o errexit

# Instala dependencias
pip install -r requirements.txt

# Ejecuta migraciones
python manage.py migrate

# Recolecta archivos estáticos (CSS, JS, imágenes)
python manage.py collectstatic --noinput
