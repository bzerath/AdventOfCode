# -*- coding: utf-8 -*-
from __future__ import unicode_literals     # Everything is UTF-8

import hashlib
import time
from multiprocessing import Pool

mot = "yzbqklnj"


class SortirDuPool(Exception):
    def __init__(self, value):
        self.value = value


def md5(string):
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()


def one_core(args):
    modulo, pop = args
    result = ""
    suffixe = modulo
    new_input = ""
    debut = time.time()
    while not result.startswith("000000"):
        #if suffixe % 100000 == 0:
        #    print time.time()-debut
        suffixe += pop
        new_input = mot + str(suffixe)
        result = md5(new_input)
    print "Résultat : {new_input}, --> {md5}, calculé en {temps} secondes".format(new_input=new_input,
                                                                                  md5=result,
                                                                                  temps=time.time()-debut)
    raise Exception

if __name__ == "__main__":

    max = 4
    for nproc in range(1, max+1):
        print nproc
        pool = Pool(processes=nproc)
        try:
            print [[i, nproc] for i in range(1, nproc+1)]
            pool.map(one_core, [[i, nproc] for i in range(1, nproc+1)])
        except Exception as e:
            print e
            if nproc != max:
                pass
            else:
                raise




