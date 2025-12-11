import requests

url = "hapi.fhir.org/baseR4"

def get_patient(patient_id: int):
    """
    Function makes an API call to the FHIR test server to fetch a Patient

    Args:
        patient_id:

    Returns:
    """
    response = requests.get(f"https://hapi.fhir.org/baseR4/Patient/{patient_id}").json()
    patient_name = response["name"]
    return patient_name

res = get_patient(47936500)
print(res)

