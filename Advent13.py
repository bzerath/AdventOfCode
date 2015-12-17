# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
from pprint import pprint
import itertools


input1 = ["Alice would gain 54 happiness units by sitting next to Bob.",
          "Alice would lose 79 happiness units by sitting next to Carol.",
          "Alice would lose 2 happiness units by sitting next to David.",
          "Bob would gain 83 happiness units by sitting next to Alice.",
          "Bob would lose 7 happiness units by sitting next to Carol.",
          "Bob would lose 63 happiness units by sitting next to David.",
          "Carol would lose 62 happiness units by sitting next to Alice.",
          "Carol would gain 60 happiness units by sitting next to Bob.",
          "Carol would gain 55 happiness units by sitting next to David.",
          "David would gain 46 happiness units by sitting next to Alice.",
          "David would lose 7 happiness units by sitting next to Bob.",
          "David would gain 41 happiness units by sitting next to Carol."]

with open("Inputs/Advent13.txt") as fichier:
    input1 = fichier.readlines()


input_formatted = {}


for ligne in input1:
    ligne = ligne.replace(".\n","").split(" ")
    if ligne[2] == "gain":
        if ligne[0] not in input_formatted:
            input_formatted[ligne[0]] = {}
        input_formatted[ligne[0]][ligne[-1]] = int(ligne[3])
    elif ligne[2] == "lose":
        if ligne[0] not in input_formatted:
            input_formatted[ligne[0]] = {}
        input_formatted[ligne[0]][ligne[-1]] = - int(ligne[3])

pprint(input_formatted)


solutions = []
combinaisons = itertools.permutations(input_formatted.keys()[1:])
prenom_tete = input_formatted.keys()[0]
for combi in combinaisons:
    value = 0
    temp = prenom_tete
    for suivant in combi:
        value += input_formatted[temp][suivant] + input_formatted[suivant][temp]
        temp = suivant
    value += input_formatted[prenom_tete][combi[-1]] + input_formatted[combi[-1]][prenom_tete]
    solutions.append([value, prenom_tete, combi])

solutions.sort()
print solutions[-1]

