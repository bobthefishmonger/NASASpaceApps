from Events import Environment, make_base

import requests
import json

API_key = "bG9GfKhtF8rwFTdMRNMMHqWBKCD6ChRD7mz7bj7J"

url = "https://ccmc.gsfc.nasa.gov/DONKI-API/get/FLR"

params = {
    "startDate": "2026-09-16",
    "endDate": "2026-11-15",
    "api_key": API_key
}

response = requests.get(url, params=params)


if response.status_code == 200:
    m_class = [f for f in response.json() if f.get("classType", "").upper().startswith("M")]
    
    print(f"found {len(m_class)} M-class flares.")
    probability = round(len(m_class) / 60, 2)
    print("probability =", probability)
    if m_class:
        print(json.dumps(m_class[0], indent=2))
else:
    print(f"error {response.status_code}: {response.text}")




class RandomHazards:
    def __init__(self, environment, buildings, storm_chance=0.01, flare_chance=probability):
        self.environment = environment
        self.buildings = buildings
        self.storm_chance = storm_chance      # chance per tick (0.01 = 1%)
        self.flare_chance = flare_chance
        self.rng = environment.rng 
