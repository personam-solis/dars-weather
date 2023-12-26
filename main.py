#!/usr/bin/env python3

"""
Run the primary interface of the program including a user interface.

This should primarily call on the other modules for references
"""

import tkinter as tk
# import globalDecorators as gd
import datetime
import json
import os
from cryptography.fernet import Fernet


# Variables
user_agent_header = 'dars-weather.com kevin.phate@gmail.com'
base_weather_url = 'https://api.weather.gov'
current_dir = os.path.abspath(os.path.dirname(__file__))

# All keys encrypted with Fernet
with open(os.path.join(current_dir, "keys.json")) as keys_file:
    all_keys = json.load(keys_file)


def main():
    # Run the main part of the program. Takes no arguments
    print(all_keys['google_api'])


if __name__ == '__main__':
    # Execute main code
    main()
