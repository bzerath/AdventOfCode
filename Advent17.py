# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
from itertools import permutations, combinations





if __name__ == "__main__":
    #containers = [20, 15, 10, 5, 5]
    containers = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
    mini_size = len(containers)
    nombre = 0
    for i in range(len(containers)):
        for combi in combinations(containers, i):
            if sum(combi) == 150:
                mini_size = min(len(combi), mini_size)

    for combi in combinations(containers, mini_size):
        if sum(combi) == 150:
            nombre += 1



    print nombre




