#!/usr/bin/env python3

import unittest
import json
import os
import earth_weather
from cryptography.fernet import Fernet

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(f"{current_dir}/..")
print(f"Current Dir: {current_dir} \nParent Dir: {parent_dir}")

# Get Responses for test
with open(os.path.join(current_dir, "responses.json")) as responses_file:
    responses = json.load(responses_file)

# Get encrypted API Keys
with open(os.path.join(parent_dir, "keys.json")) as keys_file:
    all_keys = json.load(keys_file)

# Set up the user responses
geo = earth_weather.get_location(responses['globals']['google_api_key'],
                                 responses['user_input']['location'])


class MyTestCase(unittest.TestCase):

    def test_location_info(self):
        print('Test location_info')
        self.assertEqual(round(geo['lat'], 2), responses['geo']['lat'],
                         'Latitude was incorrect.')
        self.assertEqual(round(geo['lng'], 2), responses['geo']['lng'],
                         'Longitude was incorrect.')


if __name__ == '__main__':
    unittest.main()
