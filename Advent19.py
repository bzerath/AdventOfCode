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
    # Explanation:
    #   - Every transformation is in the form $ -> µ+£ except many in the forms:
    #       - $ -> µ+ Rn +£+ Ar + (Y+¤){0-2}
    #   - Given that Rn, Ar and Y are only on the right of the equations, they are detritus, they can be skipped, returning to the form $ -> µ+£
    #   - So, we take the full molecule, in which we take out Rn, Ar and Y (2 times for Y because it is always followed by 1 atom)
    #   - We obtain a molecule 201 atoms long.
    #   - The question now is : How many switches $ -> µ+£ (so, from one atom to two) we had to make in order to switch from a 1 atom $
    #       molecule to a 201 atoms molecule ?
    #       - Given that we gain 1 atom per switch:
    #           - 1 atom to 2: 1 switch
    #           - 2 atoms to 3: 2 switches
    #           - 3 atoms to 4: 3 switches
    #           - n atoms to n+1: n switches
    #   - The answer is:
    #           number of atoms              -  number of Rn        -   number or Ar       -    2 * number of Y    - 1
    print len(list(atomGenerator(Molecule))) - Molecule.count("Rn") - Molecule.count("Ar") - 2*Molecule.count("Y") - 1



