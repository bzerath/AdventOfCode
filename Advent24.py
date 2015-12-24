# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
import itertools
import operator
import sys

Paquets = [1, 2, 3, 7, 11, 13, 17, 19, 23, 31,
           37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
           79, 83, 89, 97, 101, 103, 107, 109, 113]

# Paquets = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]


def hasSum(paquets, ngroups_left):
    """
    https://www.reddit.com/r/adventofcode/comments/3y1s7f/day_24_solutions/cy9srkh
    """
    for y in range(1, len(paquets)):
        # Increases the length of the current group
        for x in itertools.combinations(paquets, y):
            # For each combinaison
            if sum(x) == Total and ngroups_left == 2:
                # If there are 2 groups left, we don't care about the last one.
                print "1", x
                return True
            elif sum(x) == Total and hasSum(list(set(paquets) - set(x)), ngroups_left - 1):
                print "2", x
                return reduce(operator.mul, x, 1)

if __name__ == "__main__":

    Parts = 4
    Total = sum(Paquets)/Parts
    print Total
    print hasSum(Paquets, Parts)




