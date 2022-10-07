"""
Distances functions
"""
import numpy as np


def distance_quadratic(v1, v2):
    return sum((v1 - v2) ** 2) ** (1 / 2)
    distance = 0
    for i in range(len(v1) - 1):
        distance += (v1[i] - v2[i]) ** 2
    return distance**1 / 2


def distance_mean(v1, v2):
    return sum(abs(v1 - v2))
    distance = 0
    for i in range(len(v1) - 1):
        distance += abs(v1[i] - v2[i])
    return distance


def trier(L, f=lambda x, y: x < y):  # Tri par fusion
    if len(L) <= 1:
        return L
    m = int(len(L) / 2)
    L1 = trier(L[:m], f)
    L2 = trier(L[m:], f)
    Lf = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if f(L1[i], L2[j]):
            Lf.append(L1[i])
            i += 1
        else:
            Lf.append(L2[j])
            j += 1
    return Lf + L1[i:] + L2[j:]


def fusionner(L1, L2):
    L3 = L1[:]
    for x in L2:
        if not (x in L2):
            L3.append(x)
    return L3


def distance_cluster_min(c1, c2):
    min_distance_cluster = distance_quadratic(c1[0], c2[0])
    for element_c1 in c1:
        for element_c2 in c2:
            d = distance_quadratic(element_c1, element_c2)
            if d < min_distance_cluster:
                min_distance_cluster = d
    return min_distance_cluster


def distance_cluster_max(c1, c2):
    min_distance_cluster = distance_images(c1[0], c2[0])
    for element_c1 in c1:
        for element_c2 in c2:
            d = distance_quadratic(element_c1, element_c2)
            if d < min_distance_cluster:
                min_distance_cluster = d
    return min_distance_cluster


def distance_cluster_mean(c1, c2):
    dist = 0
    for element_c1 in c1:
        for element_c2 in c2:
            dist += distance_images(element_c1, element_c2)
    return dist / (len(c1) * len(c2))


def analyse(resultat, labels, k):
    # On crée les clusters, même si on ne sait pas encore à quel label il correspond
    clusters = [[] for i in range(k)]
    for i in range(len(resultat)):
        clusters[resultat[i]].append(i)

    resultats = np.zeros(len(resultat))
    # Pour chaque cluster, on regarde à quel label il correspond le plus, et on assigne donc à chaquel element ce label
    for cluster in clusters:
        l = np.zeros(k)
        for i in cluster:
            l[labels[i]] += 1
        imax = 0
        max = l[0]
        for i in range(len(l)):
            if l[i] > max:
                imax = i
        for i in cluster:
            resultats[i] = imax

    # resultats contient le label de chaque élément, on compare alors:
    nbr = 0
    for i in range(len(resultats)):
        if labels[i] == resultats[i]:
            nbr += 1
    return nbr / len(resultats)


def evaluerEfficaciteAlgo(clusters_evaluer, clusters_donnee, labels_sortie=False):
    def evaluerCluster(cluster_evaluer, cluster_donnee):
        nbr = 0
        for x in cluster_evaluer:
            for y in cluster_donnee:
                if distance(x, y) < 10 ** (-10):
                    nbr += 1
        return nbr

    success = 0
    if labels_sortie:
        labels = []
    for cluster_evaluer in clusters_evaluer:
        resultat = []
        for cluster_donnee in clusters_donnee:
            resultat.append(evaluerCluster(cluster_evaluer, cluster_donnee))
        success += max(resultat)
        if labels_sortie:
            labels.append(resultat.index(max(resultat)))
    if labels_sortie:
        return success / sum([len(x) for x in clusters_donnee]), labels
    return success / sum([len(x) for x in clusters_donnee])
