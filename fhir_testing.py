import requests

"""
Fetch some data from the FHIR endpoint using a GET request.

Get a feeling of how the API responds and get familiar with how the data works

"""

# Function performs a GET request on the H7 FHIR test server
# Extract the patients name and birthdate

#Test endpoint
api_endpoint = "https://hapi.fhir.org/baseR4/Patient/47936526"

def get_resource():
    response = requests.get(api_endpoint).json()
    return response

res = get_resource()
print(res)