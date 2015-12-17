# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8

from Tkinter import *
import time


def decode_input(string):
    if string.startswith("turn on"):
        value = 1
    elif string.startswith("turn off"):
        value = 0
    elif string.startswith("toggle"):
        value = -1

    content = string.split(" ")
    if value != -1:
        coord1 = content[2].split(",")
        coord2 = content[4].split(",")
    else:
        coord1 = content[1].split(",")
        coord2 = content[3].split(",")

    coord1 = [int(coord1[0]), int(coord1[1])]
    coord2 = [int(coord2[0]), int(coord2[1])]

    return {"lights": value,
            "from": coord1,
            "to": coord2}


class Decoration:
    def __init__(self):
        pass
        self.animation()
        """self.master = Tk()

        self.w = Canvas(self.master, width=1000, height=1000, background="white")
        self.w.pack()

        self.master.after(0, self.animation)

        self.master.mainloop()"""

    def animation(self):
        ma_matrice = matrix(1000, 1000)
        with open("Advent6.txt", "r") as fichier:
            ligne = fichier.readline()
            while ligne != "":
                infos = decode_input(ligne.replace("\n", ""))
                ma_matrice.set_rectangle(infos["from"][0],
                                         infos["from"][1],
                                         infos["to"][0],
                                         infos["to"][1],
                                         infos["lights"])
                """if ma_matrice.get(infos["from"][0], infos["from"][1]) == 1:
                    color = "blue"
                else:
                    color = "white"
                self.w.create_rectangle(infos["from"][0],
                                        infos["from"][1],
                                        infos["to"][0],
                                        infos["to"][1],
                                        fill=color)
                self.w.update()
                time.sleep(0.1)"""
                ligne = fichier.readline()
        somme = 0
        for ligne in ma_matrice.matrice:
            somme += sum(ligne)

        print somme




class matrix:
    def __init__(self, largeur, hauteur):
        matrice_1 = [0]*largeur
        self.matrice = []
        for i in range(hauteur):
            self.matrice.append(matrice_1[:])

    def set(self, x, y, value):
        if value == 1:
            self.on(x, y)
        elif value == 0:
            self.off(x, y)
        elif value == -1:
            self.toggle(x, y)

    def on(self, x, y):
        self.matrice[y][x] += 1

    def off(self, x, y):
        if self.matrice[y][x] > 0:
            self.matrice[y][x] -= 1

    def toggle(self, x, y):
        self.matrice[y][x] += 2

    def get(self, x, y):
        return self.matrice[y][x]

    def set_rectangle(self, x1, y1, x2, y2, value):
        for ordonnee in range(y1, y2+1):
            for abscisse in range(x1,x2+1):
                self.set(abscisse, ordonnee, value)


if __name__ == "__main__":

    deco = Decoration()






