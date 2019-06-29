import requests
import pprint

URL = "https://maps.googleapis.com/maps/api/geocode/json"
API = "PASTE YOUR GOOGLE MAP API KEY HERE"

# Geocoding
resp = requests.get(URL, params={
    "address": "Mysuru",
    "key": API
})

if resp.status_code == 200:
    resp_dict = resp.json()

    lat = resp_dict["results"][0]["geometry"]["location"]["lat"]
    lng = resp_dict["results"][0]["geometry"]["location"]["lng"]
    print(f"Latitude: {lat}, Longitude: {lng}")
    import webbrowser
    webbrowser.open_new_tab(
        f"https://www.google.co.in/maps?q=Mysuru")
else:
    print("Your Request Failed " + resp.status_code)

# Reverse Geocoding
resp = requests.get(URL, params={
    "latlng": f"{lat},{lng}",
    "key": API
})
if resp.status_code == 200:
    print("Most Accurate Address")
    resp_dict = resp.json()
    print(resp_dict["results"][0]["formatted_address"])
    print(resp_dict["results"][0]["types"][0])

    if len(resp_dict["results"]) > 1:
        print("Least Accurate Address")
        print(resp_dict["results"][len(resp_dict["results"]) - 1]
              ["formatted_address"])
        print(resp_dict["results"]
              [len(resp_dict["results"]) - 1]["types"][0])
