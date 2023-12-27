#!/usr/bin/env python3

"""
Get the weather data for the location chosen by the user. This leverages the
Google cloud API to get the GeoJSON. Limit its use to avoid having to pay for
things.
The Weather API is from the National Weather Service (NWS) api.weather.gov

Google Map API is needed to convert location to a geojson.
"""

import requests
import json
import googlemaps
# import globalDecorators as gd


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


def nsw_url(base_url: str, geo_location: dict, date_given: str) -> str:
    """
    Generate a URL to the National Weather Service (NSW) API. The API does not
    accept more than four decimal places for the lat lng when connecting to the
    API so always floor the result.

    Args:
        base_url (str): The base URL of the NSW API
        geo_location (dict): Keys - lat, lng
        date_given (str): The date that the user entered converted into
            YYYY-MM-DDTHH:MM:SSZ

    Returns:
        str: Built URL
    """

    return f""


def main():
    # Run the main part of the program. Takes no arguments
    # user_args = gd.user_input()
    # gd.set_logging(user_args)
    pass


if __name__ == '__main__':
    # Execute main code
    main()
