# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
import time
import timeit

def divide_groups(string):
    groups = []
    temp = string[0]
    for i in xrange(1, len(string)):
        if string[i] == string[i-1]:
            temp += string[i]
        else:
            groups.append(temp)
            temp = string[i]
    groups.append(temp)
    return groups


def look_and_say_old(string):
    groups = divide_groups(string)
    say = ""
    for i in range(len(groups)):
        if i % 100000 == 0:
            print "group {i}/{long}".format(i=i, long=len(groups))
        group = groups[i]
        say = "".join([say, str(len(group)), group[0]])
    return say


def look_and_say(string):
    say = "".join(["".join([str(len(group)), group[0]]) for group in divide_groups(string)])
    return say


def fur_et_a_mesure(string):
    temp = string[0]
    compteur = 1
    liste = []
    if len(string) > 1:
        for i in xrange(1, len(string)):
            if string[i] == temp:
                compteur += 1
            else:
                liste.append(str(compteur))
                liste.append(temp)
                compteur = 1
            temp = string[i]
        liste.extend([str(compteur), temp])
    else:
        liste = ["1", temp]

    output = "".join(liste)
    return output


def method1():
    out_str = ''
    for num in xrange(loop_count):
        out_str += str(num)
    return out_str
def method4():
    str_list = []
    for num in xrange(loop_count):
        str_list.append(str(num))
    out_str = ''.join(str_list)
    return out_str
def method6():
    out_str = ''.join([str(num) for num in xrange(loop_count)])
    return out_str
def method7():
    out_str = ''.join(str(num) for num in xrange(loop_count))
    return out_str

loop_count = 80000

if __name__ == "__main__":
    string = "1113122113"
    debut = time.time()
    """method1()

    print 'method1=', timeit.timeit(method1, number=10)
    print 'method4=', timeit.timeit(method4, number=10)
    print 'method6=', timeit.timeit(method6, number=10)
    print 'method7=', timeit.timeit(method7, number=10)"""

    for i in range(50):
        #string = look_and_say(string)
        string = fur_et_a_mesure(string)
        #print i, "done, ", len(string), time.time() - debut

    print len(string), time.time() - debut



