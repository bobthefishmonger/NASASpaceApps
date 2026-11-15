from Events import Environment
import os
import requests
import json
import numpy

from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('APIKEY')

url = "https://ccmc.gsfc.nasa.gov/DONKI-API/get/FLR"

params = {
    "startDate": "2026-09-16",
    "endDate": "2026-11-15",
    "api_key": api_key
}

response = requests.get(url, params=params)


if response.status_code == 200:
    m_class = [f for f in response.json() if f.get("classType", "").upper().startswith("M")]
    
    print(f"found {len(m_class)} M-class flares.")
    probability = round(len(m_class) / 60, 2)
    print("probability =", probability)
    if m_class:
        print(json.dumps(m_class[0]))
else:
    print(f"error {response.status_code}: {response.text}")




class RandomHazards:
    def __init__(self, environment, buildings, storm_chance=0.01, flare_chance=probability):
        self.environment = environment
        self.buildings = buildings
        self.storm_chance = storm_chance  
        self.flare_chance = flare_chance
        self.rng = environment.rng 

    def tick(self):
        alerts = []
        if self.rng.random() < self.storm_chance:   
            alerts.append(self.environment.activate_sand_storm(self.buildings))
        if self.rng.random() < self.flare_chance:    
              alerts.append(self.environment.activate_solar_flare(self.buildings))
        return alerts
