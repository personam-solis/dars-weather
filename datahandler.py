#!/usr/bin/env python3

import psycopg2 as pg2
import pandas as pd
import globalDecorators as gd
# temp
import json
import os


# temp
def import_example(file: str) -> dict:
    """
    Import an example file to be used as a test for how to write to db

    Args:
        file: local filepath to example file

    Returns:
        dict: geoJSON representation of the example
    """
    with open(file) as jsonfile:
        data = json.load(jsonfile)

    return data


def main():
    # Run the main part of the program. Takes no arguments
    # temp
    current_dir = os.path.abspath(os.path.dirname(__file__))
    import_example(os.path.join(current_dir, 'example.geojson'))


if __name__ == '__main__':
    # Execute main code
    main()
