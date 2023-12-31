#!/usr/bin/env python3

"""
Get the weather data for the location chosen by the user. This leverages the
Google cloud API to get the GeoJSON. Limit its use to avoid having to pay for
things.
The Weather API is from the National Weather Service (NWS) api.weather.gov

Google Map API is needed to convert location to a geojson.
"""

import requests
import googlemaps


def get_location(api_key: str, input_location: str) -> dict:
    """
    Get the location in Longitude and Latitude based on the user input. This uses
    the Google Maps API to convert location to a lat/long.

    Args:
        api_key (str): The Google Maps API Key
        input_location (str): User's Input Location. This will be a concat of
            City, State, Country.

    Returns:
        geo_location (dict): Keys - lat, lng
    """

    # Connect to the Google API
    gmaps = googlemaps.Client(key=api_key)

    # Geocoding an address
    geocode_result = gmaps.geocode(input_location)

    return geocode_result[0]['geometry']['location']


def nsw_url(base_url: str, geo_location: dict) -> str:
    """
    Generate a URL to the National Weather Service (NSW) API. The API does not
    accept more than four decimal places for the lat lng when connecting to the
    API so always floor the result.

    Args:
        base_url (str): The base URL of the NSW API
        geo_location (dict): Keys - lat, lng

    Returns:
        str: Built URL
    """

    return f"{base_url}/points/{geo_location['lat']},{geo_location['lng']}"


def get_weather_station(api_url: str, api_header: dict) -> str:
    """
    Retrieve the weather station ID used to get the weather data. This will perform
    three API calls to the NWS API.

    Args:
        api_url (str): URL generated based on location and time
        api_header (dict): Header for the request

    Returns:
        dict: The weather data
    """

    try:
        # Get response with all properties associated with geo
        property_request = requests.get(api_url, headers=api_header).json()

        # Get the cluster of observation stations
        observation_stations = property_request["properties"]["observationStations"]

        # Get the closest observation statin
        nearby_stations = requests.get(url=observation_stations,
                                       headers=api_header).json()

        # Get the station ID of closet one
        return nearby_stations['features'][0]['properties']["stationIdentifier"]

    except (requests.exceptions.RequestException, requests.JSONDecodeError) as error:
        print(f"An error occurred connecting to the server\n{error}")


def get_weather_data(base_url: str, api_header: dict, station_id: str) -> dict:
    """
    Retrieve the weather from the NSW API and return the data as a dictionary.
    This requires two requests. One that obtains the "properties" to grab the
    weather URL, then using that URL pull the full data.

    Args:
        base_url (str): Base URL of the NSW
        api_header (dict): Header for the request
        station_id (str): ID retrieved closest to the cluster

    Returns:
        data (dict): JSON formatted weather data
    """
    try:
        return requests.get(url=f"{base_url}/stations/{station_id}/observations",
                            headers=api_header).json()

    except (requests.exceptions.RequestException, requests.JSONDecodeError) as error:
        print(f"An error occurred connecting to the server\n{error}")


if __name__ == '__main__':
    # Dont do anything if called
    pass
