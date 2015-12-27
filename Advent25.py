# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # Everything is UTF-8
import numpy as np
from pprint import pprint

def compute_next(number):
    return (number * 252533) % 33554393

Row = 2981
Col = 3075

if __name__ == "__main__":
    np.set_printoptions(linewidth=200)

    codes = np.zeros((2, 2), dtype=np.long)
    codes[0, 0] = 20151125
    print codes

    precedent = codes[0, 0]

    row = 2
    col = 1
    while True:
        if row % 100 == 0 and col % 100 == 0:
            print row, col
        codes[row-1, col-1] = compute_next(precedent)
        precedent = codes[row-1, col-1]

        # Next diagonal
        if row == 1:
            codes = np.c_[codes, np.zeros(col)]
            codes = np.r_[codes, [np.zeros(col+1)]]
            row = col+1
            col = 1
        else:
            row -= 1
            col += 1

        if row == Row and col == Col:
            print compute_next(precedent)
            break



