#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

# List for files on the os
files = []

for file in os.listdir():
    if file == "radx.py" or file == "vacc.key" or file == "vaccine.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("vacc.key", "rb") as vaccine:
    key = vaccine.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_cure = Fernet(key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_cure)