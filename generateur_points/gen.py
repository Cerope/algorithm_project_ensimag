#!/usr/bin/env python3
"""Cree une serie de points aleatoires ainsi qu'une distance"""

from random import random, randint

with open('test.pts', 'w') as fh:
    fh.write('0.15')
    for i in range(1000):
        x = random()
        y = random()
        fh.write('{} {}\n'.format(x, y))
