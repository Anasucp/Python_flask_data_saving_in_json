



import json
import os

DATA_FILE = "data/person.json"

def read_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def write_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=2)
