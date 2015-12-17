# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
import json
from pprint import pprint


def analyse_data_dico(dico):
    somme = 0
    for cle in dico:
        somme += analyse_data(dico[cle])
        if dico[cle] == "red":
            return 0
    return somme



def analyse_data(data):
    somme = 0
    if type(data) == int:
        somme += data
    elif type(data) == str:
        pass
    elif type(data) == dict:
        somme += analyse_data_dico(data)
    elif type(data) == list:
        for sous_obj in data:
            somme += analyse_data(sous_obj)
    return somme


if __name__ == "__main__":
    with open("Advent12.json") as data_file:
        data_json = json.load(data_file, encoding="utf-8")

    #pprint(data_json)

    total = 0

    data_json2 = [1, 2, 3, 4, 5, 6,
                 [1, 2, 3],
                 {"cle": 1,
                  "cle2": [1, 2, 3],
                  3: "red"}
                 ]
    #print sum(data_json)

    for objet in data_json:
        total += analyse_data(objet)

    print total

