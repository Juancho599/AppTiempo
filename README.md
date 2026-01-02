AppTiempo

AppTiempo es una aplicación desarrollada en Python con libreria Flask, que permite consultar el clima actual de cualquier ciudad mediante la API de OpenWeatherMap

El proyecto incluye contenedorización con Docker y plantillas HTML simples para mostrar la información en un navegador.

Funcionalidades

Búsqueda de clima por ciudad.

Muestra temperatura, sensación térmica, humedad y estado del cielo.

Compatible con múltiples ubicaciones alrededor del mundo.

Preparado para ejecutarse en Docker.

Interfaz web sencilla con Flask + HTML (templates).

Tecnologías utilizadas

Lenguaje: Python 3

Framework: Flask

API: OpenWeatherMap

Frontend: HTML + Jinja2 (templates)

Contenedores: Docker

Dependencias: requirements.txt

Instalación y uso

1. Clonar el repositorio
git clone https://github.com/Juancho599/AppTiempo.git

2. Posicionarse en a la carpeta AppTiempo  
cd AppTiempo

3. Dentro de la carpeta AppTiempo, crear un entorno virtual con: 
python -m venv venv

4. Activá el entorno virtual desde la Terminal de tu S.O.
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

5. Instalar dependencias en la Terminal
pip install -r requirements.txt                                                                                                  ó en caso de que tengas Python con otras versiones:  python3 -m pip install -r requirements.txt 


6. Configurar la API Key de OpenWeatherMap

Crea un archivo llamado .env dentro AppTiempo con el contenido:

API_KEY=TU_API_KEY_DE_OPENWEATHER

Podés obtener una API Key gratuita en: https://openweathermap.org/appid

7. Luego mueve el archivo .env hacia .gitignore

8. Ejecutar la aplicación localmente
python MainTiempo.py


La aplicación la podes ejecutar en la url:
http://127.0.0.1:5000

Uso con Docker

Construir la imagen:

docker build -t app-tiempo


Ejecutar el contenedor:

docker run -d -p 5000:5000 --env API_KEY=TU_API_KEY_DE_OPENWEATHER app-tiempo
ó si usas Docker Desktop, en la seccion de Imagenes, vas a encontrar el nombre de AppTiempo. Tenes que hacer click en "Start"

Abrir en el navegador:
http://localhost:5000

<img width="1140" height="512" alt="FrontMain" src="https://github.com/user-attachments/assets/5a036aed-24b5-4c1e-802a-c88f2b70f536" />
<img width="929" height="341" alt="NombreDeCiudad" src="https://github.com/user-attachments/assets/899557c5-7b8e-475f-8f59-ed1be15cfba1" />
<img width="926" height="412" alt="DatosClima" src="https://github.com/user-attachments/assets/66bca90c-e142-4168-84cc-7a54d49fb071" />


Para este proyecto utilicé:

Integración de APIs con OpenWeatherMap.

Desarrollo de aplicaciones web con Flask.

Template HTML con Jinja2.

Contenerización con Docker.

Manejo de variables de entorno con .env.

Mejoras a futuro:

 Agregar pronóstico extendido de varios días.

 Implementar selección de idioma y unidades (°C/°F).

 Agregar logs para depuración.

 Desplegar en la nube con Heroku y AWS
