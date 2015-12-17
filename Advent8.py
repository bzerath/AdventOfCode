# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8

with open("Advent8.txt","r") as fichier:
    lignes = fichier.readlines()

"""lignes = [r'""',
          r'"abc"',
          r'"aaa\"aaa"',
          r'"\x27"']
#          r'"jctcqra\"\x05dhlydpqamorqjsijt\\xjdgt"'"""

somme_code = 0
somme_char = 0

r"""for i in range(len(lignes)):
    lignes[i] = lignes[i].replace("\n", "")

    somme_code += len(lignes[i])
    ligne_avant = lignes[i]

    lignes[i] = lignes[i][1:-1]  # On enlève les quotes sur les côtés
    lignes[i] = lignes[i].replace(r"\\", "/")
    lignes[i] = lignes[i].replace(r'\"', '"')
    while r"\x" in lignes[i]:
        place = lignes[i].index(r"\x")
        lignes[i] = lignes[i].replace(lignes[i][place:place+4], "#")

    print ligne_avant, len(ligne_avant), lignes[i], len(lignes[i])

    somme_char += len(lignes[i])"""


for i in range(len(lignes)):
    lignes[i] = lignes[i].replace("\n", "")
    somme_code += len(lignes[i])
    ligne_avant = lignes[i]
    lignes[i] = "/"+lignes[i][:-1]+'/"'
    lignes[i] = lignes[i].replace(r'\"', '///"')
    lignes[i] = lignes[i].replace(r'\\', '////')
    lignes[i] = lignes[i].replace(r'\x', '//x')

    print ligne_avant, len(ligne_avant), lignes[i], len(lignes[i])+2
    somme_char += len(lignes[i]) + 2


print somme_char - somme_code

