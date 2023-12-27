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
import argparse
from cryptography.fernet import Fernet


# Variables
user_agent_header = 'dars-weather.com kevin.phate@gmail.com'
base_weather_url = 'https://api.weather.gov'
current_dir = os.path.abspath(os.path.dirname(__file__))

# All keys encrypted with Fernet
with open(os.path.join(current_dir, "keys.json")) as keys_file:
    imported_keys = json.load(keys_file)


def user_input() -> argparse.Namespace:
    """
    Get a user input and convert to an argparse namespace object.

    Returns:
        argparse.Namespace
    """
    parser = argparse.ArgumentParser(description="""
Input additional arguments for troubleshooting and for decrypting the keys. 

Ensure that before testing API connections the dev PIN in used; when the application
is built create a salted password
    """, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--key", "-k", metavar="FERNET_KEY",
                        help="Key used to decrypt secrets using Fernet")
    parser_args = parser.parse_args()

    return parser_args


def secret_decrypter(encryption_key: str, ciphertext: str) -> str:
    """
    Take in an encrypted key and decrypt it into a usable string. This is used
    to securely store keys encrypted then decrypt as needed. This requires the
    key to be encrypted used with Fernet using the 'encryption' module

    Args:
        encryption_key (str): Asynchronous encryption key
        ciphertext (str): The encrypted ciphertext

    Returns:
        decrypted_string (str)
    """

    # Create Fernet object using the Asynchronous key
    fernet = Fernet(encryption_key)

    # Decrypt
    return fernet.decrypt(ciphertext).decode()


def main():
    # Run the main part of the program. Takes no arguments
    user_args = user_input()


if __name__ == '__main__':
    # Execute main code
    main()
