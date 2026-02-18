import re

# Lecture du fichier 
with open(r'c:\wamp64\www\Test_cours\travail en python\AWS test pratique reStart\journal_bord.txt', 'r') as f:
     seq = f.read()
     # on affiche le nombre de lignes du journal 
nbre_lignes =len(seq.splitlines())
print(f"le nombre de lignes du journal : {nbre_lignes}")
 # Affichage **uniquement les lignes contenant le mot `"Alerte"` ou `"alerte"`*
for line in seq.splitlines():
     if "Alerte" in line.lower ():
         print(line)
print(f"---Alerte detectee---{len(line)}")
# Création d'un nouveau fichier `journal_bord_alerte.txt` qui contient uniquement les lignes du journal contenant le mot `"Alerte"` ou `"alerte"`*
with open('journal_bord_alerte.txt','w') as f :
     for line in seq.splitlines():
        if "alerte" in line.lower():
            f.write(line + "\n")
            print(line)
print("---le fichier journal_bord_alerte.txt a ete cree---")
