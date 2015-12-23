# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
from itertools import permutations, combinations
import timeit



def p2():
    """
    better one.
    :return:
    """
    def mini_size_of_solution(containers, value):
        for solution_size in xrange(len(containers)):
            for combi in combinations(containers, solution_size):
                if sum(combi) == value:
                    return solution_size

    containers = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
    value = 150
    nombre = 0
    mini_size = mini_size_of_solution(containers, value)
    for combi in combinations(containers, mini_size):
        if sum(combi) == value:
            nombre += 1
    return nombre

def p1():
    containers = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
    value = 150
    mini_size = len(containers)
    nombre = 0
    for i in range(len(containers)):
        for combi in combinations(containers, i):
            if sum(combi) == value:
                nombre += 1
    return nombre



if __name__ == "__main__":
    #containers = [20, 15, 10, 5, 5]

    print "p1", p1()
    print "p2", p2()




