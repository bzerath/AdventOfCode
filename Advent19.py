# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
from pprint import pprint
import string

Molecule = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"
minuscules = string.ascii_lowercase
majuscules = string.ascii_uppercase

def atomGenerator(molecule):
    for i in range(len(molecule)-1):
        if molecule[i] in minuscules:
            continue
        else:
            if molecule[i] in majuscules and molecule[i+1] in majuscules:
                yield molecule[i], i
            else:
                yield molecule[i:i+2], i
    if molecule[-1] not in minuscules:
        yield molecule[-1], len(molecule)-1


if __name__ == "__main__":
    transformation = {}
    with open("Inputs/Advent19.txt") as fichier:
        lignes = fichier.readlines()

    # lignes = ["H => HO", "H => OH", "O => HH"]

    for ligne in lignes:
        ligne = ligne.replace("\n", "").split(" ")
        if ligne[0] in transformation:
            transformation[ligne[0]].append(ligne[2])
        else:
            transformation[ligne[0]] = [ligne[2]]
    pprint(transformation)

    solutions = []
    tests = 0
    for atome, i in atomGenerator(Molecule):
        if atome in transformation:
            for possibilite in transformation[atome]:
                solutions.append("".join([Molecule[:i], possibilite, Molecule[i+len(atome):]]))
    solutions = list(set(solutions))

    print len(solutions)


    # Part 2
    # thanks https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4h7ji
    print len(list(atomGenerator(Molecule))) - Molecule.count("Rn") - Molecule.count("Ar") - 2*Molecule.count("Y") - 1



