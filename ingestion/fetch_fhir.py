import requests

url = "hapi.fhir.org/baseR4"

def get_patient(patient_id: int):
    """
    Function makes an API call to the FHIR test server to fetch a Patient

    Args:
        patient_id (int): identifier for the patient resource

    Returns:
        raw JSON for the patient from the FHIR server
    """
    response = requests.get(f"https://hapi.fhir.org/baseR4/Patient/{patient_id}").json()
    # patient_name = response["name"]
    return response

def get_observations(observation_id: int):
    """
    Function makes an API call the FHIR test server to fetch an Observation resource.
    Observations can be anything from lab results, patient characteristics, vitals,
    clinical findings, imaging results, social history, etc. THese are all used to
    support the patient diagnosis.

    Args:
        observation_id:

    Returns:
        raw JSON observation

    """
    try:
        response = requests.get(f"https://hapi.fhir.org/baseR4/Observation/{observation_id}", timeout=5).json()
        return response
    except requests.RequestException as e:
        return {"error": "Error fetching observations", "details":str(e)}

res = get_observations(582454)
print(res)








