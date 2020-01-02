#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv
from math import sqrt
from geo.point import Point
import sys


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
    sys.setrecursionlimit(10000)
    cote = distance / sqrt(2)
    max_x_abs = abs(points[0].coordinates[0])
    max_y_abs = abs(points[0].coordinates[1])
    for p in points:
        if abs(p.coordinates[0]) > max_x_abs:
            max_x_abs = abs(p.coordinates[0])
        if abs(p.coordinates[1]) > max_y_abs:
            max_y_abs = abs(p.coordinates[1])
    maxi = max(max_x_abs, max_y_abs)
    eps = 0.01
    while eps >= cote:
        eps = eps / 2
    maxi += eps # Pour eviter des soucis de frontiere
    grand_cote = 2*maxi
    nbr_carres_par_cote = grand_cote // cote
    if grand_cote % cote != 0:
        nbr_carres_par_cote += 1 # Cas ou il y a des ptits carres en plus

    carres = dict()
    tailles = []

    for point in points:
        # coord_x va donc de 0 a grand_cote//2
        if point.coordinates[0] < 0:
            coord_x = (maxi + point.coordinates[0])//cote
        else:
            coord_x = (maxi + point.coordinates[0])//cote # Inutile, a verifier mais pas besoin

        if point.coordinates[1] < 0:
            coord_y = (maxi - point.coordinates[1])//cote
        else:
            coord_y = (maxi - point.coordinates[1])//cote # Inutile, a verifier mais pas besoin

        if (coord_x, coord_y) in carres.keys():
            carres[(coord_x, coord_y)].append(point)
        else:
            carres[(coord_x, coord_y)] = [point]

    for case in carres.keys():
        compteur = 0
        dernier = carres[case].pop()
        if dernier == "flag":
            carres[case].append(dernier)
        else:
            carres[case].append(dernier)
            carres[case].append("flag")
            compteur = recherche(carres, case, distance)
            tailles.append(compteur)
    tailles.sort(reverse=True)
    print(tailles)


def recherche(carres, case, distance):
    compteur = len(carres[case])-1
    # if (case[0]-1, case[1]-2) in carres.keys():
    #     reponse = est_voisin(carres, carres[case], carres[(case[0]-1, case[1]-2)], distance)
    #     compteur += reponse
    for i in range(-2, 3, 1):
        for j in range(-2, 3, 1):
            if (i, j) != (0, 0) and (i, j) != (-2, -2) and (i, j) != (2, 2) and (i, j) != (-2, 2) and (i, j) != (2, -2):
                if (case[0]-i, case[1]-j) in carres.keys():
                    reponse = est_voisin(carres, case, (case[0]-i, case[1]-j), distance)
                    # print(reponse)
                    compteur += reponse
    return compteur
    #
    #               (1)|   2   |   3  |   4  |   (5)
    #             -----|-------|------|------|-------
    #               6  |   7   |   8  |   9  |   10
    #             -----|-------|------|------|-------
    #               11 |   12  | (13) |  14  |   15
    #             -----|-------|------|------|-------
    #               16 |   17  |  18  |  19  |   20
    #             -----|-------|------|------|-------
    #              (21)|   22  |  23  |  24  |   (25)
    #                  |       |      |      |
    #               1  |   2   |   3  |   4  |   5
    #
    #
    #                  LA CASE COURANTE EST LA 13

            # est_voisin renvoie un compteur


def est_voisin(carres, case_ref, case_test, distance):
    """Verifie si la case fait partie de la composante connexe voulue"""
    compteur = 0
    dernier = carres[case_test].pop()
    if dernier == "flag":
        carres[case_test].append(dernier)
        return 0
    else:
        carres[case_test].append(dernier)
        for point_ref in carres[case_ref][:len(carres[case_ref])-1]:
            for point_test in carres[case_test]:
                if point_test.distance_to(point_ref) <= distance:
                    carres[case_test].append("flag")
                    compteur += recherche(carres, case_test, distance)
                    return compteur
        return 0

def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
