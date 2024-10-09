def ecrire_fichier(chemin_fichier, lignes):
    with open(chemin_fichier, 'w') as f:
        for ligne in lignes:
            f.write(ligne + "\n")

# Utilisation
chemin_fichier = 'chemin/vers/votre/fichier.txt'
lignes = ['Ligne 1', 'Ligne 2', 'Ligne 3']
ecrire_fichier(chemin_fichier, lignes)
