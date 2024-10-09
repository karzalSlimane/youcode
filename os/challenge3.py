import os
import shutil

def copier_fichiers_csv(source, destination):
    os.makedirs(destination, exist_ok=True)
    for fichier in os.listdir(source):
        if fichier.endswith('.csv'):
            shutil.copy(os.path.join(source, fichier), destination)

# Utilisation
source = 'chemin/vers/repertoire/source'
destination = 'chemin/vers/repertoire/destination'
copier_fichiers_csv(source, destination)
