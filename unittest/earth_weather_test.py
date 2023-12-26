import unittest
import json
import os
import earth_weather
from ..earth_weather import *


print(os.path.join(os.getcwd(), "responses.json"))


# Get Responses for test
with open(os.path.join(os.path.dirname(__file__), "responses.json")) as responses_file:
    responses = json.load(responses_file)

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
