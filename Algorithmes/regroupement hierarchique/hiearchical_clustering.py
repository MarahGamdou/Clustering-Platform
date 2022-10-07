import numpy as np
import random as rd
import math
import copy

##étapes:
# on met une donnée par cluster (donc on crée N clusters)
# on afficher /stocker les étapes de fusion de clusters
# on arrete après N-1 fusions

### Entrée
Tab_Entree = [rd.randint(0, 100) for i in range(20)]
parametre_distance_cluster = input("entrer : max ou min")  ##mean à faire

###distance_element
def distance_element(e1, e2):
    return abs(e1 - e2)


###distance_cluster
def distance_cluster(c1, c2):

    # distance min
    if parametre_distance_cluster == "min":
        min_distance_cluster = distance_element(c1[0], c2[0])
        for element_c1 in c1:
            for element_c2 in c2:
                if distance_element(element_c1, element_c2) < min_distance_cluster:
                    min_distance_cluster = distance_element(element_c1, element_c2)
        return min_distance_cluster

    # distance min
    elif parametre_distance_cluster == "max":
        max_distance_cluster = distance_element(c1[0], c2[0])
        for element_c1 in c1:
            for element_c2 in c2:
                if distance_element(element_c1, element_c2) > max_distance_cluster:
                    max_distance_cluster = distance_element(element_c1, element_c2)
        return max_distance_cluster


###fusion des clusters


def fusion(ligne, i):
    c = {}
    for element in range(N):
        if ligne[element] in c.keys():
            c[int(ligne[element])] = c[int(ligne[element])] + [Tab_Entree[element]]
        else:
            c[int(ligne[element])] = [Tab_Entree[element]]
    print(c)

    min = math.inf
    for j in range(len(c)):
        for l in range(j + 1, len(c)):
            if distance_cluster(c[j], c[l]) < min and j != l:
                min = distance_cluster(c[j], c[l])
                indices_min = (j, l)
    l = indices_min[1]
    j = indices_min[0]
    print("l", l)
    print("j", j)
    ligne_suivante = copy.deepcopy(ligne)
    print(ligne_suivante)
    for indice in range(len(ligne_suivante)):
        if ligne_suivante[indice] == l:
            ligne_suivante[indice] = j
    print(ligne_suivante)
    print(max(ligne_suivante))
    for indice in range(len(ligne_suivante)):
        if ligne_suivante[indice] == max(ligne):
            ligne_suivante[indice] = l
    print(ligne_suivante)
    return ligne_suivante


########   main  ##########
###creation d'une matrice de similarité
N = len(Tab_Entree)
Tab_similarite = np.zeros((N, N), int)
###on met une donnée par cluster
for i in range(0, N):
    Tab_similarite[0][i] = i
###on fusionne 2 clusters à chaque passage de la ligne i à la ligne i+1 (N-1 fusions)
for i in range(N - 1):
    Tab_similarite[i + 1] = fusion(Tab_similarite[i], N - i)

print(Tab_similarite)
