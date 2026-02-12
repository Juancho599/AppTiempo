import json

from weather_client import fetch_weather
from services import parse_weather_data


def lambda_handler(event, context):
    ciudad = event.get("city")

    if not ciudad:
        return {
            "statusCode": 400,
            "body": json.dumps(
                {"error": "city parameter is required"},
                ensure_ascii=False
            )
        }

    try:
        raw_data = fetch_weather(ciudad)
        weather = parse_weather_data(raw_data)

        return {
            "statusCode": 200,
            "body": json.dumps(weather, ensure_ascii=False)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}, ensure_ascii=False)
        }


if __name__ == "__main__":
    # Test local (NO se ejecuta en Lambda)
    test_event = {"city": "Buenos Aires"}
    print(lambda_handler(test_event, None))

