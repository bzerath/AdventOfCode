# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
import timeit


class Ingredient:
    def __init__(self, nom, capacity, durability, flavor, texture, calories):
        self.nom = nom
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories


def score(qtte1, qtte2, qtte3):
    qtte4 = 100 - qtte1 - qtte2 - qtte3
    capacity = max(0, qtte1*sugar.capacity + qtte2*sprinkles.capacity + qtte3*candy.capacity + qtte4*chocolate.capacity)
    durability = max(0, qtte1*sugar.durability + qtte2*sprinkles.durability + qtte3*candy.durability + qtte4*chocolate.durability)
    flavor = max(0, qtte1*sugar.flavor + qtte2*sprinkles.flavor + qtte3*candy.flavor + qtte4*chocolate.flavor)
    texture = max(0, qtte1*sugar.texture + qtte2*sprinkles.texture + qtte3*candy.texture + qtte4*chocolate.texture)

    return capacity * durability * flavor * texture


def score_w_cal(qtte1, qtte2, qtte3):
    qtte4 = 100 - qtte1 - qtte2 - qtte3
    capacity = max(0, qtte1*sugar.capacity + qtte2*sprinkles.capacity + qtte3*candy.capacity + qtte4*chocolate.capacity)
    durability = max(0, qtte1*sugar.durability + qtte2*sprinkles.durability + qtte3*candy.durability + qtte4*chocolate.durability)
    flavor = max(0, qtte1*sugar.flavor + qtte2*sprinkles.flavor + qtte3*candy.flavor + qtte4*chocolate.flavor)
    texture = max(0, qtte1*sugar.texture + qtte2*sprinkles.texture + qtte3*candy.texture + qtte4*chocolate.texture)
    calories = max(0, qtte1*sugar.calories + qtte2*sprinkles.calories + qtte3*candy.calories + qtte4*chocolate.calories)

    if calories != 500:
        return 0
    else:
        return capacity * durability * flavor * texture


def version_net():
    return max(score_w_cal(a, b, c)
                for a in xrange(101)
                    for b in xrange(101 - a)
                        for c in xrange(101 - a - b)
                if 0 <= a+b+c <= 100)

def version_perso():
    maxi = 0
    combi = []
    for qtte1 in xrange(101):
        for qtte2 in xrange(101 - qtte1):
            for qtte3 in xrange(101-qtte1-qtte2):
                temp = score_w_cal(qtte1, qtte2, qtte3)
                if temp > maxi:
                    maxi = temp
                    combi = [qtte1, qtte2, qtte3, 101-qtte1-qtte2-qtte3]

    return maxi, combi



if __name__ == "__main__":
    sugar = Ingredient("Sugar", 3, 0, 0, -3, 2)
    sprinkles = Ingredient("Sprinkles", -3, 3, 0, 0, 9)
    candy = Ingredient("Candy", -1, 0, 4, 0, 1)
    chocolate = Ingredient("Chocolate", 0, 0, -2, 2, 8)

    print 'method net=', timeit.timeit(version_net, number=30)
    print 'method perso=', timeit.timeit(version_perso, number=30)

    print version_net()
    print version_perso()




