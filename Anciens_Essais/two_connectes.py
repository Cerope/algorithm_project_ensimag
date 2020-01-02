#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv

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
    liste_comp_conn = []

    while points != []:

        flag = False
        point_courant = points.pop()
        composante_temp = []
        composante_importante = []
        for composante in liste_comp_conn:
            for point in composante:
                if point_courant.distance_to(point) <= distance:
                    #1ere composante connexe que l'on trouve a laquelle rattacher le point
                    if not flag:
                        composante.append(point_courant) # On la rattachee
                        flag = True # On previent qu'on l'a deja rattache
                        # On previent que l'on va peut etre fusionner des composantes
                        composante_temp.append(composante)
                        composante_importante = composante
                        break # On arrete de travailler dans cette composante connexe
                    else: # Pour les autres composantes connexes, si le point a deja ete rattache
                        # On rajoute cette composante a celles qu'il faut fusionner
                        composante_temp.append(composante)
                        composante_importante += composante
                        liste_comp_conn.remove(composante)

                        break # On arrete de travailler dans cette composante connexe

        if not flag: # Si aucune composante a laquelle relier est trouvee, on en cree une nouvelle
            liste_comp_conn.append([point_courant])


        # Si flag mais pas de flag2, aucun soucis on a deja append dans la boucle
    # Apres traitement de tous les points, on trie par taille
    tailles = [len(composante) for composante in liste_comp_conn]
    tailles.sort(reverse=True)
    print(tailles)

def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
