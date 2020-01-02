#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv
from math import sqrt
from geo.point import Point


def load_instance(filename):
    """
    loads .pts file.
    returns distance limit and points.
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        points = [Point([float(f) for f in l.split(",")]) for l in lines]

    return distance, points


def print_components_sizes(distance, points):
        """
        affichage des tailles triees de chaque composante
        """
        cote = distance / sqrt(2)
        max_x_abs = max(points[0].coordinates[0])
        max_y_abs = abs(points[0].coordinates[1])
        for p in points:
            if abs(p.coordinates[0]) > max_x_abs:
                max_x_abs = abs(p.coordinates[0])
            if abs(p.coordinates[1]) > max_y_abs:
                max_y_abs = abs(p.coordinates[0])
        maxi = max(max_x_abs, max_y_abs)
        grand_cote = 2*maxi

        for point in points :
            if point.coordinates[0] < 0:
                x = (max_x_abs + point.coordinates[0])//cote
            else:
                x = point.coordinates[0]//cote

        #flag
        #def explorer_voisin
def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
