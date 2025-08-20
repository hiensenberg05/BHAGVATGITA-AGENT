google_maps_api_key = "AIzaSyBtmLlpo_pR_UyauKEENupribquXdQ3UJQ"
import requests


def check_google_maps_api_key(api_key):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": "New York",
        "key": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get("status") == "OK":
            print("API key is active and working.")
        else:
            print(f"API key error: {data.get('error_message', data.get('status'))}")
    else:
        print(f"HTTP error: {response.status_code}")

if __name__=='__main__':
    check_google_maps_api_key(google_maps_api_key)