# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 08:55:46 2020

@author: CEC
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimaore"
key = "VoWKYtJJq0DfEEeUt6O7wpb7a6uoZpnE"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)