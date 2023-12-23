#!/usr/env python3

"""
Get the weather data for the location chosen by the user. This leverages the
Google cloud API to get the GerJSON. Limit its use to avoid having to pay for
things.

Google Map API is needed to convert location to a geojson.
"""

import requests
import json
import googlemaps
from datetime import datetime
import globalDecorators as gd

user_agent = 'dars-weather.com kevin.phate@gmail.com'
base_weather_url = 'https://api.weather.gov'
GOOGLE_API_KEY = 'AIzaSyAn64xOw5SAj6JTfiE1ZaNHsFzrpYaQKug'




def main():
    # Run the main part of the program. Takes no arguments
    user_args = gd.user_input()
    gd.set_logging(user_args)


if __name__ == '__main__':
    # Execute main code
    main()
