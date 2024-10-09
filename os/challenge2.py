import os

def verifier_fichier_config(repertoire, nom_fichier='config.yaml'):
    chemin_fichier = os.path.join(repertoire, nom_fichier)
    if os.path.exists(chemin_fichier):
        with open(chemin_fichier, 'r') as f:
            contenu = f.read()
            print(contenu)
    else:
        print(f"Le fichier {nom_fichier} n'existe pas dans le répertoire.")

# Utilisation
repertoire = 'chemin/vers/votre/repertoire'
verifier_fichier_config(repertoire)
