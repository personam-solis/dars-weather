#!/usr/bin/env python3
import requests
import json


mars_weather_api_key = r"mfAdD3C6RnDp8UuzFsaT9mjI6vjIeWWbDKqCb6qE"


def get_mars_weather(api_key: str) -> dict:
    """
    Get the Mars weather data from the NASA API

    Args:
        api_key (str): API key for getting weather data

    Returns:
        json (dict): weather data
    """
    url = f"https://api.nasa.gov/insight_weather/?api_key={api_key}&feedtype=json&ver=1.0"
    get_data = requests.get(url)
    return json.loads(get_data.text)


def main():
    # Runs the main part of the program. This does not accept nor return anything
    mars_weather = get_mars_weather(mars_weather_api_key)
    print(json.dumps(mars_weather, indent=4, sort_keys=True))


if __name__ == "__main__":
    # Execute the main code
    main()
