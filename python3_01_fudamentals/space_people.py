import requests

response = requests.get('http://api.open-notify.org/astros.json')

json = response.json()

# for key, value in json.items():
#     print(f"key: {key}\nvalue: {value}\n")

for people in json["people"]:
    print(f"{people['name']} at {people['craft']}")



