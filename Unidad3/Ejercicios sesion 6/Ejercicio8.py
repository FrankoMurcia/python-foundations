import requests

endpoint = "https://dragonball-api.com/api/characters?limit=10"

try:
    response = requests.get(endpoint)
    response.raise_for_status()
    data = response.json()

    
    razas = {}

    for character in data["items"]:
        raza = character.get("race")
        if raza not in razas:
            razas[raza] = []
        razas[raza].append(character)

    
    for raza, personajes in razas.items():
        print(f"\n--- Raza: {raza} ---")
        total_ki = 0
        count = 0
        for p in personajes:
            nombre = p.get("name")
            ki_str = str(p.get("ki", "0")).replace(".", "").replace(",", "")  
            try:
                ki = int(ki_str)
            except ValueError:
                ki = 0
            print(f"Nombre: {nombre}, Ki: {ki}")
            total_ki += ki
            count += 1
        promedio_ki = total_ki / count if count > 0 else 0
        print(f"Promedio de Ki para {raza}: {promedio_ki:.2f}")

except requests.exceptions.RequestException as e:
    print(f"Error recuperando la data: {e}")
