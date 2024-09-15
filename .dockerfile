FROM python:3.11 as base_image

WORKDIR /opt/app

# Copiar los archivos necesarios
COPY ./requirements.txt .
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Inicializar Reflex
RUN reflex init

# Exponer puertos
EXPOSE 3000
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación
CMD ["reflex", "run", "--env", "prod"]