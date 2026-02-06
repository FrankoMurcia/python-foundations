import requests

endpoint = "https://dragonball-api.com/api/characters?limit=58"

try:
    response = requests.get(endpoint)
    response.raise_for_status()
    data = response.json()

    #print(data)
    for character in data["items"]:
        print(character["name"], character["race"])

except requests.exceptions.RequestException as e:
    print(f"Error recuperando la data: {e}")