import json

def save_to_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def read_from_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)