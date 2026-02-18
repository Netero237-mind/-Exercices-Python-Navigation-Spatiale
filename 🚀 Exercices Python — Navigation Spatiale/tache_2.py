import os

mission_data ='c:\\wamp64\\www\\Test_cours\\travail en python\\AWS test pratique reStart\\mission_data'
if os.path.exists(mission_data):
    print(f"le dossier mission_data existe")
else:
    print(f'le dossier mission_data n\'existe pas')

def liste_fichier(mission_data):
    try:
        
        return os.listdir(mission_data)
    except Exception:
        return []

if __name__ == "__main__":
    try:
        elements = sorted(os.listdir(mission_data))
        file = liste_fichier(mission_data)
        if file:
            print(f"le dossier contient les fichiers suivants : {file}")
            for f in file:
                print(f" {f} ")
        else:
            print(f"Aucun fichier trouvé dans le dossier {mission_data}")
    except Exception as e:
        print(f"Erreur {e}")
rapport = os.path.join(mission_data, 'rapport')
connecteur = "└── " if rapport else "├── "
extension_prefix = "    " if rapport else "│   "
        
archive = os.path.join(mission_data, 'archive')
os.makedirs(rapport, exist_ok=True)
os.makedirs(archive, exist_ok=True)
taille_bytes = os.path.getsize(mission_data)
taille_ko = taille_bytes / 1024
print(f"   {connecteur}📄 {elements} ({taille_ko:.1f} Ko)")

print(f"Les dossiers rapport et archive ont été créés avec succès.")
