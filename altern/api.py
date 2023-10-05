import requests

API_ENDPOINT = "https://api.altern.ai/v1/info.json"

def is_status_success():
    response = requests.get(API_ENDPOINT)
    if response.status_code == 200:
        data = response.json()
        return data.get("status") == "success"
    return False