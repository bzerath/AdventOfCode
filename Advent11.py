# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
import string

lenpsswd = 8
forbidden = ["i", "o", "l"]
alphabet = string.ascii_lowercase


def check_rule1(mdp):
    """
    Passwords must include one increasing straight of at least three letters,
    like abc, bcd, cde, and so on, up to xyz.
    They cannot skip letters; abd doesn't count.
    :param mdp:
    :return:
    """
    for depart in range(lenpsswd-3):
        triplet = mdp[depart:depart+3]
        if triplet in alphabet:
            return True
    return False


def check_rule2(mdp):
    for i in range(lenpsswd):
        if mdp[i] in forbidden:
            mdp = increase(mdp[:i+1])+"a"*(lenpsswd-i-1)
            return mdp
    return mdp


def check_rule3(mdp):
    result1 = False
    case1 = ""
    result2 = False
    for i in range(lenpsswd-1):
        if result1 and mdp[i] != case1 and mdp[i] == mdp[i+1]:
            result2 = True
        if mdp[i] == mdp[i+1]:
            result1 = True
            case1 = mdp[i]
    return result1 and result2


def checkcorrectness(mdp):
    return check_rule1(mdp) and check_rule3(mdp)


def next_pswd(mdp):
    mdp = check_rule2(mdp)
    mdp = increase(mdp)
    while not checkcorrectness(mdp):
        mdp = increase(mdp)
    return mdp


def increase(mdp):
    rightmost = mdp[-1]
    index_rightmost_plus_one = alphabet.index(rightmost) + 1
    if index_rightmost_plus_one < len(alphabet) and alphabet[index_rightmost_plus_one] in forbidden:
        index_rightmost_plus_one += 1
    if index_rightmost_plus_one < len(alphabet):
        return mdp[:-1]+alphabet[index_rightmost_plus_one]
    else:
        return increase(mdp[:-1])+alphabet[0]




if __name__ == "__main__":
    """mdp = "ghaaaaaa"
    print check_rule1(mdp)
    print check_rule3(mdp)"""

    print "p1", next_pswd("cqjxjnds")
    print "p2", next_pswd(next_pswd("cqjxjnds"))

