# forecast-fastapi-docker

Se creará un proyecto que se subirá a GCP mediante FASTAPI

El modelo se encontrará en la carpeta notebooks en una carpeta llamada models.

Se crea una FAST API en el archivo app para manejar todas las solicitudes HTTP a esa ruta, luego se crea
la API y se enruta, en la api es donde se realizará la predicción del modelo.


Para validar la app localmente se tienen estos comandos desde consola:


docker build -t fast-api-app6 .


docker run -p 80:80 fast-api-app7





