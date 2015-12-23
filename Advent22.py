# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
from Advent21 import Personnage
from itertools import product


def sort_standard(func):
    def wrapper(self, advers, dmg):
        # print "Lancement du sort"
        func(self, advers, dmg)
        # print "Fin du sort"
        if advers.pv <= 0:
            return True
        else:
            return False
    return wrapper


class Personnage_v2(Personnage):
    def __init__(self, attack, defense, pv, name, mana):
        Personnage.__init__(self, attack, defense, pv, name)
        self.mana = mana
        self.effects = {"Poison": -1,
                        "Shield": -1,
                        "Recharge": -1}   # {"effect_name": n° turns left, ]

        self._nb_tours_poison = 6
        self._nb_tours_shield = 6
        self._nb_tours_Recharge = 5

        self.mort_en_debut_de_tour = False

        self.mana_depensee = 0

    def joue_contre(self, advers, spell_name):
        #self.mort_en_debut_de_tour = self.apply_effect()
        #advers.mort_en_debut_de_tour = advers.apply_effect()

        if self._spell(spell_name, advers):
            return True



    def apply_effect(self):
        if min(self.pv, self.mana) <= 0:
            return True
        if self.effects["Shield"] == self._nb_tours_shield:
            self.defend_score += 7
            #print "{name} gains a Shield effect and now has {armor} armor.".format(name=self.name, armor=self.defend_score)
        elif self.effects["Shield"] == 0:
            self.defend_score -= 7
            #print "{name} loses its Shield effect.".format(name=self.name)

        if 0 < self.effects["Poison"] <= self._nb_tours_poison:
            self.pv -= 3
            #print "Poison deals 3 dmg, {pv} pv left.".format(pv=self.pv)
            if self.pv > 0:
                pass
            else:
                #print "Poison kills {name}.".format(name=self.name)
                return True

        if 0 < self.effects["Recharge"] <= self._nb_tours_Recharge:
            self.mana += 101
            #print self.name, "gains 101 mana and now has", self.mana, "mana."

        self.effects["Shield"] -= 1
        self.effects["Recharge"] -= 1
        self.effects["Poison"] -= 1

        return False

    def _spell(self, spell, advers):
        #print self.name, "spells", spell
        if spell == "MagicMissile":
            return self._MagicMissile(advers)
        elif spell == "Drain":
            return self._Drain(advers)
        elif spell == "Poison":
            return self._Poison(advers)
        elif spell == "Recharge":
            return self._Recharge()
        elif spell == "Shield":
            return self._Shield()
        elif spell == "Physique":
            return self.attack(advers)

    def _MagicMissile(self, advers):
        self.mana -= 53
        self.mana_depensee += 53
        self._attack_magic(advers, 4)

    def _Drain(self, advers):
        self.mana -= 73
        self.mana_depensee += 73
        self.pv += 2
        self._attack_magic(advers, 2)

    def _Poison(self, advers):
        self.mana -= 173
        self.mana_depensee += 173
        if advers.effects["Poison"] > 0:
            self.pv = 0
        advers.effects["Poison"] = self._nb_tours_poison

    def _Recharge(self):
        self.mana -= 229
        self.mana_depensee += 229
        if self.effects["Recharge"] > 0:
            self.pv = 0
        self.effects["Recharge"] = self._nb_tours_Recharge

    def _Shield(self):
        self.mana -= 113
        self.mana_depensee += 113
        if self.effects["Shield"] > 0:
            self.pv = 0
        self.effects["Shield"] = self._nb_tours_shield

    @sort_standard
    def _attack_magic(self, advers, dmg):
        advers.pv -= dmg

    def attack(self, advers):
        # print self.name, "attacks", advers.name
        advers.pv -= max(self.attack_score - advers.defend_score, 1)

    def __str__(self):
        return "- {nom} has {pv} hit points, {armor} armor, {mana} mana".format(nom=self.name,
                                                                                pv=self.pv,
                                                                                armor=self.defend_score,
                                                                                mana=self.mana)


def test_enchainement(enchainements):
    for enchainement in enchainements:
        enchainement = list(enchainement)
        boss = Personnage_v2(9, 0, 51, "Boss", 1)
        mage = Personnage_v2(0, 0, 50, "Mage", 500)
        #print enchainement
        for sort in enchainement:
            #print "-- Player turn --"
            #print mage
            #print boss
            mage.pv -= 1  # Part 2
            mage_mort = mage.apply_effect()
            boss_mort = boss.apply_effect()
            if not mage_mort:
                if not boss_mort:
                    mage.joue_contre(boss, sort)
                else:
                    print "1",mage.mana_depensee, enchainement
                    return True
            else:
                break

            #print "-- Boss turn --"
            #print mage
            #print boss
            mage_mort = mage.apply_effect()
            boss_mort = boss.apply_effect()
            if not mage_mort:
                if not boss_mort:
                    boss.joue_contre(mage, "Physique")
                else:
                    print mage.mana_depensee, enchainement
                    return True
            else:
                break

    return False



if __name__ == "__main__":
    sorts = ["MagicMissile", "Drain", "Poison", "Recharge", "Shield"]

    nb_enchainements = 1
    while True:
        nb_enchainements += 1
        print nb_enchainements
        enchainements = product(sorts, repeat=nb_enchainements)
        #print list(enchainements)
        if test_enchainement(enchainements):
            break






