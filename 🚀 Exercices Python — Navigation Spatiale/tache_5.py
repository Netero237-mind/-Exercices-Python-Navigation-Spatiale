import os
import shutil
from datetime import date
import shutil as sh

def main():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    mission_dir = os.path.join(base_dir, 'mission_data')
    rapports_dir = os.path.join(mission_dir, 'rapports')
    archives_dir =os.path.join(mission_dir, 'archives')
    journaux_src = os.path.join(mission_dir, 'journaux')
    # Vérifier existence dossiers / créer si nécessaire

    os.makedirs(rapports_dir, exist_ok=True)
    os.makedirs(archives_dir, exist_ok=True)
    # Copier journal_bord.txt dans archives en le renommant avec la date du jour
    today_str = date.today().strftime('%Y-%m-%d')
    journal_dst = os.path.join(archives_dir, f'journal_bord_{today_str}.txt')
    try:
        shutil.copy2(os.path.join(journaux_src, 'journal_bord.txt'), journal_dst)
        copied = True
        print(f"✅ Journal copié dans les archives : {journal_dst}")
    except FileNotFoundError:
        copied = False
        print(f"❌ Journal non trouvé dans {journaux_src}")
    # Créer un rapport de mission
    rapport_path =os.path.join(rapports_dir,"rapport_systeme.txt")
    with open(rapport_path, "w", encoding="utf-8") as rf:
        rf.write(f"Répertoire courant du script : {os.getcwd()}\n\n")

        rf.write("Variables d'environnement (filtrées PYTHON / PATH) :\n")
        for k, v in sorted(os.environ.items()):
            if "PYTHON" in k.upper() or "PATH" in k.upper():
                rf.write(f"{k}={v}\n")
        rf.write("\n")
        # Espace disque du disque contenant base_dir
        try:
            usage =sh.disk_usage(base_dir)
            total_gd =usage.total / (1024 ** 3)
            used_gd =usage.used / (1024 ** 3)
            free_gd =usage.free / (1024 ** 3)
            rf.write(f"Espace disque du disque contenant le script :\n")
            rf.write(f"Total : {total_gd:.2f} GB\n")
        except Exception as e:
            rf.write(f"Erreur lors de la récupération de l'espace disque : {e}\n")
    #Resumer des operations
    print("\n--- Résumé des opérations ---")
    if copied:
        print(f"Copie effectuée : {journal_dst}")
    else:
        print("Le journal de bord n'a pas pu être copié car il est introuvable.")
    print(f"Rapport de mission créé : {rapport_path}")
if __name__ == "__main__":    main()