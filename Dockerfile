FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Define un volumen para los paquetes descargados
VOLUME /usr/local/share/argos-translate

# Ejecuta el script para descargar los paquetes necesarios
RUN python downloadPackages.py

EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
