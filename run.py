#!/usr/bin/env python3

"""From Google IT Automation with Python Course 6, Lab 4

run.py processes textual data into jason format for automatic upload to the Django rest endpoint."""


import os
import requests

source_dir = "supplier-data/descriptions/"
url = "http://localhost/fruits/"
images_dir = "supplier-data/images/"

def format_fruit(text_file):
  with open(os.path.join(source_dir,text_file),"r") as file:
    fruit_list_info = file.read().split("\n")
    fruit_info = {
      "name" : fruit_list_info[0],
      "weight" : int(fruit_list_info[1].strip(" lbs")),
      "description" : fruit_list_info[2],
      "image_name" : os.path.splitext(text_file)[0] + ".jpeg"
    }
  return fruit_info

files_to_post_list = os.listdir(source_dir)

for file in files_to_post_list:
  fruit_deets = format_fruit(file)
  info_to_post = requests.post(url,json=fruit_deets)
  info_to_post.raise_for_status()
  print(info_to_post.status_code)

