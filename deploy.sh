#!/bin/bash

# Navegar al directorio de tu proyecto
cd ~/cd_django/

# Actualizar el repositorio
git pull origin master

# Activar el entorno virtual
source ~/cd/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones de la base de datos
python manage.py migrate

# Recopilar archivos estáticos
python manage.py collectstatic --noinput
