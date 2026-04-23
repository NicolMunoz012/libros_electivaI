#!/usr/bin/env bash
# Exit on error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos
python proyecto/manage.py collectstatic --no-input

# Aplicar migraciones de base de datos
python proyecto/manage.py migrate