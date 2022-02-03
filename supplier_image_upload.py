#!/usr/bin/env python3

"""From Google automation course 6 lab 4: this script will
upload the files from the folder created with the changed images
in changeImage.py"""

import requests
import os
import sys

source = "supplier-data/images/"
url = "http://localhost/upload/"

for image in os.listdir(source):
    if image.endswith(".jpeg"):
        with open(os.path.join(source,image), 'rb') as opened:
            r = requests.post(url,files={'file':opened})