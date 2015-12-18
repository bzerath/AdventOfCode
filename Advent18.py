# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def total(grid, x, y):
    left =        0 if x == 0            else grid[y, x-1]
    right =       0 if x == len(grid[y])-1 else grid[y, x+1]
    top =         0 if y == 0            else grid[y-1, x]
    bottom =      0 if y == len(grid)-1    else grid[y+1, x]

    topleft =     0 if (x == 0              or y == 0)           else grid[y-1, x-1]
    topright =    0 if (x == len(grid[0])-1 or y == 0)           else grid[y-1, x+1]
    bottomright = 0 if (x == len(grid[0])-1 or y == len(grid)-1) else grid[y+1, x+1]
    bottomleft =  0 if (x == 0              or y == len(grid)-1) else grid[y+1, x-1]

    return [top, topright, right, bottomright, bottom, bottomleft, left, topleft]

def update_mat(data):
    global life
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newLife = life.copy()

    for y in xrange(len(life)):
        for x in xrange(len(life[y])):
            temp_total = sum(total(life, x, y))

            # apply Conway's rules
            if life[y, x] == 1:
                if (temp_total < 2) or (temp_total > 3):
                    newLife[y, x] = 0
            else:
                if temp_total == 3:
                    newLife[y, x] = 1
    # update data
    mat.set_data(newLife)
    life = newLife
    return [mat]

def update(life):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newLife = life.copy()

    for y in xrange(len(life)):
        for x in xrange(len(life[y])):
            temp_total = sum(total(life, x, y))

            # apply Conway's rules
            if life[y, x] == 1:
                if (temp_total < 2) or (temp_total > 3):
                    newLife[y, x] = 0
            else:
                if temp_total == 3:
                    newLife[y, x] = 1
    # update data
    return newLife



if __name__ == "__main__":
    life = []
    with open("Inputs/Advent18.txt") as fichier:
        ligne = fichier.readline()
        while ligne != "":
            temp = []
            for character in ligne.replace("\n",""):
                temp.append(1 if character == "#" else 0)
            life.append(temp)
            ligne = fichier.readline()

    life = np.asarray(life)
    life = life.astype(int)

    """print life
    life = update(life)
    print life"""


    fig, ax = plt.subplots()
    mat = ax.matshow(life)
    ani = animation.FuncAnimation(fig, update_mat, interval=50, save_count=50)
    plt.show()


