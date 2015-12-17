# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8

vowels = "aeiou"

forbidden = ["ab", "cd", "pq", "xy"]


def check_if_3_vowels_old(string):
    number = 0
    for vowel in vowels:
        for letter in string:
            if vowel == letter:
                number += 1
    if number >= 3:
        return True
    else:
        return False


def check_letter_twice_old(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True


def check_forbidden_old(string):
    for forb in forbidden:
        if forb in string:
            return True
    return False


def check_nice_old(string):
    if not check_forbidden_old(string) and check_if_3_vowels_old(string) and check_letter_twice_old(string):
        return True
    else:
        return False


def check_letter_twice(string):
    for i in range(len(string)-1):
        temp = string[i]+string[i+1]
        if temp in string[i+2:]:
            return True
    return False


def check_letter_repeat(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False


def check_nice(string):
    if check_letter_twice(string) and check_letter_repeat(string):
        return True
    else:
        return False


if __name__ == "__main__":
    compteur = 0
    with open("Advent5.txt", "r") as fichier:
        ligne = fichier.readline()
        while ligne != "":
            if check_nice(ligne):
                compteur += 1
            ligne = fichier.readline()
    print compteur
