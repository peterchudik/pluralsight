import requests
from pprint import pprint as pp

city = "Nitra"
url = "http://api.weatherapi.com/v1/current.json?key=77d900f9124644f792e193840242002 &q=" + city + "&aqi=no"

response = requests.get(url)

json = response.json()

condition_text = json.get("current").get("condition").get("text")
temp_c = json.get("current").get("temp_c")

print(f"Current weather in {city} is {condition_text} and {temp_c} degrees")
