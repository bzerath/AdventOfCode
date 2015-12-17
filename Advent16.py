# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8



class Tante:
    def __init__(self, number, children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes):
        self.number = number
        self.children = children
        self.cats = cats
        self.samoyeds = samoyeds
        self.pomeranians = pomeranians
        self.akitas = akitas
        self.vizslas = vizslas
        self.goldfish = goldfish
        self.trees = trees
        self.cars = cars
        self.perfumes = perfumes

    def check_si_cest_elle(self):
        if (self.children is None or self.children == 3) \
                and (self.cats is None or self.cats >= 7)\
                and (self.samoyeds is None or self.samoyeds == 2)\
                and (self.pomeranians is None or self.pomeranians <= 3)\
                and (self.akitas is None or self.akitas == 0)\
                and (self.vizslas is None or self.vizslas == 0)\
                and (self.goldfish is None or self.goldfish <= 5)\
                and (self.trees is None or self.trees >= 3)\
                and (self.cars is None or self.cars == 2)\
                and (self.perfumes is None or self.perfumes == 1):
            return self.number
        else:
            return False


    def __str__(self):
        return "Aunt Sue #{number} has {children} children, " \
                                      "{cats} cats, " \
                                      "{samoyeds} samoyeds, " \
                                      "{pomeranians} pomeranians, " \
                                      "{akitas} akitas, " \
                                      "{vizslas} vizslas, " \
                                      "{goldfish} goldfish, " \
                                      "{trees} trees, " \
                                      "{cars} cars, " \
                                      "{perfumes} perfumes".format(number=self.number,
                                                                   children=self.children,
                                                                   cats=self.cats,
                                                                   samoyeds=self.samoyeds,
                                                                   pomeranians=self.pomeranians,
                                                                   akitas=self.akitas,
                                                                   vizslas=self.vizslas,
                                                                   goldfish=self.goldfish,
                                                                   trees=self.trees,
                                                                   cars=self.cars,
                                                                   perfumes=self.perfumes)


def parse_line(string):
    string_space = string.replace(":","").replace(",","").split(" ")
    #print string_space
    number = string_space[1]
    children = None
    cats = None
    samoyeds = None
    pomeranians = None
    akitas = None
    vizslas = None
    goldfish = None
    trees = None
    cars = None
    perfumes = None
    for attribute in (2, 4, 6):
        if string_space[attribute] == "children":
            children = int(string_space[attribute+1])
        elif string_space[attribute] == "cats":
            cats = int(string_space[attribute+1])
        elif string_space[attribute] == "samoyeds":
            samoyeds = int(string_space[attribute+1])
        elif string_space[attribute] == "pomeranians":
            pomeranians = int(string_space[attribute+1])
        elif string_space[attribute] == "akitas":
            akitas = int(string_space[attribute+1])
        elif string_space[attribute] == "vizslas":
            vizslas = int(string_space[attribute+1])
        elif string_space[attribute] == "goldfish":
            goldfish = int(string_space[attribute+1])
        elif string_space[attribute] == "trees":
            trees = int(string_space[attribute+1])
        elif string_space[attribute] == "cars":
            cars = int(string_space[attribute+1])
        elif string_space[attribute] == "perfumes":
            perfumes = int(string_space[attribute+1])
        else:
            print string_space[attribute], "unknown !"

    return Tante(number, children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes)


if __name__ == "__main__":

    with open("Inputs/Advent16.txt") as fichier:
        lignes = fichier.readlines()

    tantes = []
    for ligne in lignes:
        tante = parse_line(ligne.replace("\n", ""))
        if tante.check_si_cest_elle():
            print tante
        tantes.append(tante)



