import requests # type: ignore

def obtener_clima(ciudad, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        clima = datos['weather'][0]['description']
        temperatura = datos['main']['temp']
        humedad = datos['main']['humidity']
        viento = datos['wind']['speed']

        print(f"\n📍 Clima en {ciudad.capitalize()}:")
        print(f"🌡️ Temperatura: {temperatura}°C")
        print(f"💧 Humedad: {humedad}%")
        print(f"🌬️ Viento: {viento} m/s")
        print(f"🔎 Descripción: {clima}")
    else:
        print(f"\n❌ Error al obtener datos del clima: {respuesta.status_code}")
        if respuesta.status_code == 404:
            print("Verifica el nombre de la ciudad.")
        elif respuesta.status_code == 401:
            print("Tu API key no es válida o expiró.")

if __name__ == "__main__":
    load_dotenv()

    api_key = os.getenv("API_KEY")

    if not api_key:
        raise RuntimeError(
            "API_KEY no encontrada. "
            "Creá un archivo .env con la variable API_KEY"
        )

    ciudad = input("Ingrese el nombre de una ciudad: ")
    obtener_clima(ciudad, api_key)

