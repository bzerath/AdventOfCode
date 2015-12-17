# -*- coding: utf-8 -*-
from __future__ import unicode_literals     # Everything is UTF-8


def calculerSurface(dimension):
    l, w, h = dimension
    mini = min([l*w, w*h, h*l])
    aire = 2*l*w + 2*w*h + 2*h*l + mini
    return aire

def calculerRuban(dimension):
    l, w, h = dimension
    dimension.sort()
    wrapping = dimension[0]*2 + dimension[1]*2
    bow = l*w*h
    return wrapping + bow



with open("Advent2.txt", "r") as fichier:
    dimensions = fichier.readlines()
for i in range(len(dimensions)):
    dimensions[i] = dimensions[i].replace("\n","").split("x")
    for u in range(len(dimensions[i])):
        dimensions[i][u] = int(dimensions[i][u])


# dimensions = [[2,3,4], [1,1,10]]

totalruban = 0
totalpapier = 0
for dim in dimensions:
    #print calculerSurface(dim)
    #print calculerRuban(dim)
    totalruban += calculerRuban(dim)
    totalpapier += calculerSurface(dim)
print "papier",totalpapier
print "ruban",totalruban


