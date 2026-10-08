#!/bin/sh

# 1. Aplicar migraciones en PostgreSQL
echo "Aplicando migraciones..."
python manage.py migrate --no-input

# 2. Recolectar archivos estáticos para WhiteNoise
echo "Recolectando estáticos..."
python manage.py collectstatic --no-input

# 3. Iniciar el servidor web de producción
echo "Iniciando Gunicorn..."
exec gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 2 --log-file -