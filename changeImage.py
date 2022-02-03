#!/usr/bin/env python3

"""changeImage will process Google Course 6 lab 4's into proper format."""

import os, sys  
from PIL import Image


import os
import sys
from PIL import Image

src_folder = "supplier-data/images/"

def change_image(og_img):
  original = Image.open(og_img)
  new_img = original.convert(mode="RGB").resize((600,400))
  new_name = os.path.splitext(og_img)[0] + ".jpeg"
  new_img.save(new_name)
  print("successfully changed to jpeg: " + new_name)

for pic in os.listdir(src_folder):
  if pic.endswith(".tiff"):
    change_image(src_folder + pic)


