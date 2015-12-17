# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8


my_input = ["123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i"]

resultats = {}


def assignation_simple(depart, arrivee):
    global resultats
    try:
        depart = int(depart)
        resultats[arrivee] = depart
        return True
    except ValueError:
        if depart in resultats.keys():
            resultats[arrivee] = resultats[depart]
            return True
    return False


def assignation_inverse(depart, arrivee):
    global resultats
    try:
        depart = int(depart)
        resultats[arrivee] = 65536 - depart
        return True
    except ValueError:
        if depart in resultats.keys():
            resultats[arrivee] = 65535 - resultats[depart]
            return True
    return False


def assignation_operation(depart1, depart2, operateur, arrivee):
    global resultats
    depart1_type = ""
    depart2_type = ""
    try:
        depart1 = int(depart1)
        depart1_type = "int"
    except ValueError:
        depart1_type = "var"
    try:
        depart2 = int(depart2)
        depart2_type = "int"
    except ValueError:
        depart2_type = "var"

    if operateur == "AND":
        if (depart1_type == "var" and depart1 in resultats.keys()) and (depart2_type == "var" and depart2 in resultats.keys()):
            resultats[arrivee] = resultats[depart1] & resultats[depart2]
            return True
        elif (depart1_type == "int") and (depart2_type == "var" and depart2 in resultats.keys()):
            resultats[arrivee] = depart1 & resultats[depart2]
            return True
        elif (depart2_type == "int") and (depart1_type == "var" and depart1 in resultats.keys()):
            resultats[arrivee] = depart2 & resultats[depart1]
            return True
        elif (depart2_type == "int") and (depart1_type == "int"):
            resultats[arrivee] = depart2 & depart1
            return True

    elif operateur == "OR":
        if (depart1_type == "var" and depart1 in resultats.keys()) and (depart2_type == "var" and depart2 in resultats.keys()):
            resultats[arrivee] = resultats[depart1] | resultats[depart2]
            return True
        elif (depart1_type == "int") and (depart2_type == "var" and depart2 in resultats.keys()):
            resultats[arrivee] = depart1 | resultats[depart2]
            return True
        elif (depart2_type == "int") and (depart1_type == "var" and depart1 in resultats.keys()):
            resultats[arrivee] = depart2 | resultats[depart1]
            return True
        elif (depart2_type == "int") and (depart1_type == "int"):
            resultats[arrivee] = depart2 | depart1
            return True

    elif operateur == "LSHIFT":
        if (depart1_type == "var" and depart1 in resultats.keys()) and (depart2_type == "var" and depart2 in resultats.keys()):
            resultats[arrivee] = resultats[depart1] << resultats[depart2]
            return True
        elif (depart1_type == "int") and (depart2_type == "var" and depart2 in resultats.keys()):
            resultats[arrivee] = depart1 << resultats[depart2]
            return True
        elif (depart2_type == "int") and (depart1_type == "var" and depart1 in resultats.keys()):
            resultats[arrivee] = resultats[depart1] << depart2
            return True
        elif (depart2_type == "int") and (depart1_type == "int"):
            resultats[arrivee] = depart1 << depart2
            return True
    elif operateur == "RSHIFT":
        if (depart1_type == "var" and depart1 in resultats.keys()) and (depart2_type == "var" and depart2 in resultats.keys()):
            resultats[arrivee] = resultats[depart1] >> resultats[depart2]
            return True
        elif (depart1_type == "int") and (depart2_type == "var" and depart2 in resultats.keys()):
            resultats[arrivee] = depart1 >> resultats[depart2]
            return True
        elif (depart2_type == "int") and (depart1_type == "var" and depart1 in resultats.keys()):
            resultats[arrivee] = resultats[depart1] >> depart2
            return True
        elif (depart2_type == "int") and (depart1_type == "int"):
            resultats[arrivee] = depart1 >> depart2
            return True
    return False



fichier = open("Advent7.txt","r")
my_input = fichier.readlines()
fichier.close()

taille_fichier = len(my_input)

nombre_passage = 1

while len(my_input) > 0:
    print "Passage #"+str(nombre_passage)
    for numligne in range(len(my_input)):
        try:
            ligne = my_input[numligne].replace("\n", "").split(" ")
            if len(ligne) == 3:
                if assignation_simple(ligne[0], ligne[2]):
                    print "Ligne", ligne, "résolue (assignation simple)"
                    print resultats
                    del my_input[numligne]
                    break
            elif len(ligne) == 4:
                if assignation_inverse(ligne[1], ligne[3]):
                    print "Ligne", ligne, "résolue (assignation inverse)"
                    print resultats
                    del my_input[numligne]
                    break
            elif len(ligne) == 5:
                if assignation_operation(ligne[0], ligne[2], ligne[1], ligne[4]):
                    print "Ligne", ligne, "résolue (operation)"
                    print resultats
                    del my_input[numligne]
                    break
        except OverflowError:
            print my_input[numligne].replace("\n", "").split(" ")
            print resultats["da"]
            raise
    nombre_passage += 1

print resultats["a"]

