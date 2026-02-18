import json
import os
file_path = "mission_data/mission.json"
def charger_json_securise(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            print(f"✅Le fichier a été chargé avec succès.")
            return data
    except FileNotFoundError:
        print(f"❌Erreur : le fichier '{file_path}' est introuvable.")
    except json.JSONDecodeError:
        print(f"❌Erreur : le fichier '{file_path}' contient des données JSON invalides.")
    except KeyError:
        print(f"❌Erreur : le fichier '{file_path}' ne contient pas les clés attendues.")
        return None
with open("mission_data/corrompu.json", "w") as f:
    f.write("{nom: valeur_sans_guillemets}")
    data = charger_json_securise("mission_data/corrompu.json")
data = charger_json_securise("mission_data/fantome.json")
data = charger_json_securise("mission_data/missions.json")

