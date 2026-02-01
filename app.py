import requests # type: ignore

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


