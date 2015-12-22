# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
import timeit
import numpy as np


def version_numpy():
    maisons = np.full((2300000,), 10, dtype=np.int)
    for elf in xrange(2, len(maisons)):
        for maison in xrange(elf, len(maisons), elf):
            maisons[maison] += elf*10

    return np.amin(np.where(maisons >= 33100000))


def version_python():
    maisons = [10]*2300000
    for elf in xrange(2, len(maisons)):
        for maison in xrange(elf, len(maisons), elf):
            maisons[maison] += elf*10

    return min([i for i in xrange(len(maisons)) if maisons[i] >= 33100000])


def version_numpy_p2():
    maisons = np.full((2300000,), 10, dtype=np.int)
    for elf in xrange(2, len(maisons)):
        nbHousesDelivered = 0
        for maison in xrange(elf, len(maisons), elf):
            maisons[maison] += elf*11
            nbHousesDelivered += 1
            if nbHousesDelivered == 50:
                break

    return np.amin(np.where(maisons >= 33100000))


def version_python_p2():
    maisons = [10]*2300000
    for elf in xrange(2, len(maisons)):
        nbHousesDelivered = 0
        for maison in xrange(elf, len(maisons), elf):
            maisons[maison] += elf*11
            nbHousesDelivered += 1
            if nbHousesDelivered == 50:
                break

    return min([i for i in xrange(len(maisons)) if maisons[i] >= 33100000])


if __name__ == "__main__":

    print "Numpy =", timeit.timeit(version_numpy, number=10)
    print version_numpy()
    print "Python =", timeit.timeit(version_python, number=10)
    print version_python()

    print "Numpy =", timeit.timeit(version_numpy_p2, number=10)
    print version_numpy_p2()
    print "Python =", timeit.timeit(version_python_p2, number=10)
    print version_python_p2()





