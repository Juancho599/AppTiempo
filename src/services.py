def parse_weather_data(data):
    return {
        "ciudad": data.get("name"),
        "temperatura": data["main"]["temp"],
        "humedad": data["main"]["humidity"],
        "viento": data["wind"]["speed"],
        "descripcion": data["weather"][0]["description"]
    }
