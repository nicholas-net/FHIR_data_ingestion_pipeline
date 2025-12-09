import requests
import json

"""
Fetch some data from the FHIR endpoint using a GET request.

Get a feeling of how the API responds and get familiar with how the data works

"""

# Function performs a GET request on the H7 FHIR test server
# Extract the patients name and birthdate

#Test endpoint
api_endpoint = "https://hapi.fhir.org/baseR4/Patient/47936526"

def parse_json_obj():
    with open("schemas/patient_example.json", "r") as file:
        data = json.load(file)
    return data

def get_resource():
    response = requests.get(api_endpoint).json()
    return response

print(parse_json_obj())

