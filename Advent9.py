# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
import itertools

distances = {}



def decodeLigne(ligne):
    global distances
    ligne = ligne.replace("\n","")
    ligne = ligne.split(" ")
    lieu1, lieu2, distance = [ligne[0], ligne[2], int(ligne[4])]
    if lieu1 not in distances:
        distances[lieu1] = {}
    distances[lieu1][lieu2] = distance
    if lieu2 not in distances:
        distances[lieu2] = {}
    distances[lieu2][lieu1] = distance


if __name__ == "__main__":
    with open("Advent9.txt", "r") as fichier:
        lignes = fichier.readlines()

    #lignes = ["London to Dublin = 464",
    #          "London to Belfast = 518",
    #          "Dublin to Belfast = 141"]

    for ligne in lignes:
        decodeLigne(ligne)
    print distances

    combinaisons = itertools.permutations(distances.keys())
    chemins = []

    for combinaison in combinaisons:
        distance_temp = 0
        for i in range(len(combinaison)-1):
            distance_temp += distances[combinaison[i]][combinaison[i+1]]
        chemins.append((distance_temp, combinaison))

    chemins.sort()
    print chemins[-1]







