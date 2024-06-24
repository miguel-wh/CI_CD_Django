#!/bin/bash

# Navegar al directorio de tu proyecto
cd ~/CI_CD_Django/

echo "*******Inicia - git pull******"
# Actualizar el repositorio
git pull github master
echo "*******Termina - git pull******"

# Activar el entorno virtual
source ~/cicd/bin/activate

# Instalar dependencias
echo "*******Inicia - Instalar dependencias******"
pip install -r requirements.txt
echo "*******Termina - Instalar dependencias******"

# Aplicar migraciones de la base de datos
echo "*******Inicia - Aplicar migraciones******"
python manage.py migrate
echo "*******Inicia - Aplicar migraciones******"

echo "*******Inicia - Reiniciar servicio******"
echo "*******Termina - Reiniciar servicio******"
# Recopilar archivos estáticos
#python manage.py collectstatic --noinput
