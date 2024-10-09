import os

def combiner_fichiers_textes(repertoire):
    contenu_total = ""
    for fichier in os.listdir(repertoire):
        if fichier.endswith('.txt'):
            with open(os.path.join(repertoire, fichier), 'r') as f:
                contenu_total += f.read() + "\n"
    return contenu_total

# Utilisation
repertoire = './'
texte_combiner = combiner_fichiers_textes(repertoire)
print(texte_combiner)
