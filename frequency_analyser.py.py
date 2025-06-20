import os
print ("repertoire courant:",os.getcwd())

from collections import Counter
def _init_(self, octet,frequence):
    self.octet = octet
    self.frequence = frequence

def _repr_(self):
    return f"{self.octet}: {self.frequence}"

def lire_fichier_et_compter(fichier):
    with open(fichier,'rb') as f:
        contenu = f.read()
        frequence = Counter(contenu)
    return frequence

def creer_file_priorite(frequence):
    file = [Noeud(k,v) for k,v in frequence.items()]
    file_triee = sorted(file,key = lambda n: n.frequence)
    return file_triee
def analyser_fichier(fichier):
    freq = lire_fichier_et_compter(fichier)
    file_priorite = creer_file_priorite(freq)
    for noeud in file_priorite:
        print(noeud)

# analyser_fichier("frequence_texte.txt")
