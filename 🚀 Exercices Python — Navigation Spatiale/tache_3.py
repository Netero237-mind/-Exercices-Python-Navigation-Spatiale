import json
import os

from files.JsonFileHander import readJsonFile
file_path = "mission_data/mission.json"
def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data  = json.load(json_file)
    except IOError:
        print("NE PEUT PAS LIRE LE FICHIER")
        return None
    return data
data = read_json_file(file_path)

with open("mission_data/mission.json",'r',encoding='utf-8') as json_file:
    contenu = json_file.read()
    data  = json.loads(contenu)
if data is None:
    print("Aucune donnée chargée.")
else:
    missions = data.get('missions') or data.get('mission')

budget_total = 0
mission_plus_longue = None
mission_plus_courte = None
duree_max = 0
duree_min = float('inf')

for mission in missions:
    id_mission = mission['id']
    nom = mission['nom']
    destination = mission['destination']
    duree = mission['duree_jours']
    equipage_count = len(mission['equipage'])
    budget = mission['budget_millions_usd']

    print(f"[{id_mission}] {nom} → {destination} | {duree} jours | Équipage : {equipage_count} | Budget : {budget:,} M$")
     # Accumulation pour les calculs
    budget_total += budget
     # Trouver mission la plus longue
    if duree > duree_max:
        duree_max = duree
        mission_plus_longue = nom
         
    # Trouver mission la plus courte
    if duree < duree_min:
        duree_min = duree
        mission_plus_courte = nom
print(f"\n Budget total : {budget_total:,} millions USD")
print(f"\n Mission la plus LONGUE : [{mission_plus_longue}] {duree_max} jours")
print(f" Mission la plus COURTE : [{mission_plus_courte}] {duree_min} jours")
