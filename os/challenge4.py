import os

def creer_structure_repertoires(principal, sous_repertoires):
    os.makedirs(principal, exist_ok=True)
    for nom in sous_repertoires:
        os.makedirs(os.path.join(principal, nom), exist_ok=True)

# Utilisation
principal = 'chemin/vers/repertoire/principal'
sous_repertoires = ['sous1', 'sous2', 'sous3']
creer_structure_repertoires(principal, sous_repertoires)
