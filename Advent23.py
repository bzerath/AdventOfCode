# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8


def instruction(instr, value):
    if instr == "hlf":
        return value/2
    elif instr == "tpl":
        return value*3
    elif instr == "inc":
        return value+1


if __name__ == "__main__":
    registers = {"a": 1, "b": 0}

    with open("Inputs/Advent23.txt") as fichier:
        lignes = fichier.readlines()

    #lignes = ["inc a", "jio a, +2", "tpl a", "inc a"]

    numLigne = 0
    while numLigne < len(lignes):
        ligne = lignes[numLigne].replace("\n", "").replace(",", "").split(" ")
        print ligne
        if ligne[0][0] != "j":
            registers[ligne[1]] = instruction(ligne[0], registers[ligne[1]])
        else:
            if ligne[0] == "jmp":
                numLigne += int(ligne[1])
                continue
            elif ligne[0] == "jie":
                if registers[ligne[1]] % 2 == 0:
                    numLigne += int(ligne[2])
                    continue
            elif ligne[0] == "jio":
                if registers[ligne[1]] == 1:
                    numLigne += int(ligne[2])
                    continue
        numLigne += 1

    print registers


