# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
from itertools import permutations, combinations, product

class Personnage:
    def __init__(self, attack, defense, pv, name):
        self.name = name
        self.attack_score = attack
        self.defend_score = defense
        self.pv = pv

    def attack(self, advers):
        advers.pv -= max(self.attack_score - advers.defend_score, 1)
        if advers.pv <= 0:
            return True
        else:
            return False

    def wearItem(self, objet):
        self.attack_score += objet[1]
        self.defend_score += objet[2]


def testStats(personnage):
    boss = Personnage(8, 2, 100, "Boss")

    while True:
        if not player.attack(boss):
            if not boss.attack(player):
                pass
            else:
                print "Boss wins !"
                return False
        else:
            print "Players wins !"
            return True


if __name__ == "__main__":
    Weapons = {"Dagger": [8, 4, 0],
               "Shortsword": [10, 5, 0],
               "Warhammer": [25, 6, 0],
               "Longsword": [40, 7, 0],
               "Greataxe": [74, 8, 0]}

    Armor = {"None": [0, 0, 0],
             "Leather": [13, 0, 1],
             "Chainmail": [31, 0, 2],
             "Splintmail": [53, 0, 3],
             "Bandedmail": [75, 0, 4],
             "Platemail": [102, 0, 5]}

    Rings = {"None": [0, 0, 0],
             "Damage +1": [25, 1, 0],
             "Damage +2": [50, 2, 0],
             "Damage +3": [100, 3, 0],
             "Defense +1": [20, 0, 1],
             "Defense +2": [40, 0, 2],
             "Defense +3": [80, 0, 3]}

    dualRing = list(combinations(Rings.keys(), 2))
    uniqueRing = [("None", a) for a in Rings.keys()]
    ringsCombinations = dualRing + uniqueRing

    solutions = []

    for weapon, armor, jewel in product(Weapons.keys(), Armor.keys(), ringsCombinations):
        price = Weapons[weapon][0] + Armor[armor][0] + Rings[jewel[0]][0] + Rings[jewel[1]][0]
        #print weapon, armor, jewel, price
        solutions.append((price, {'weapon': Weapons[weapon],
                                  "armor": Armor[armor],
                                  "ring1": Rings[jewel[0]],
                                  "ring2": Rings[jewel[1]]}))
    solutions.sort()
    for solution in solutions:
        player = Personnage(0, 0, 100, "Player")
        for objet in solution[1]:
            player.wearItem(solution[1][objet])

        if testStats(player):
            print solution
            break




