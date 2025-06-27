#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = list(reader)
            
        with open("data.json", "w") as json_file:
            json.dump(data_list, json_file)
            
        return True
    
    except Exception:
        return False
