import numpy as np
import time as time
from random import randint

BDDs = {"mnist": False, "simpleND": True}

print("=========================")
# On importe les bases de données
print("Importation des bases de données")
if BDDs["mnist"]:
    print("[✔] Importation du MNIST")
    import ddb.mnist as mnist
else:
    print("[✘] Importation du MNIST")
if BDDs["simpleND"]:
    print("[✔] Importation de la base de données simple en N-D")
    import ddb.simpleND as simpleND
else:
    print("[✘] Importation de la base de données simple en N-D")

# On importe les algorithmes de clustering
print("\n\nImportation des algorithmes de clustering")
print("[✔] K-means")
import algos.kmeans as kmeans

print("[✔] K-Neighbors")
import algos.kNeighbors as kNeighbors

print("[✔] DBSCAN")
import algos.DBSCAN as DBSCAN

print("[✔] Regroupement Hierarchique")
import algos.regroupementHierarchique as regroupHierar

import algos.functions as fct

print("=========================")
print("\n\n\n\n")

"""
Variables de développement
"""
nbrInitial = 1000
nbrTester = 1000

## MNIST
if BDDs["mnist"]:

    print("Comparaison des algorithmes de clustering sur le MNIST")

    # Cluster d'initialisation
    clusters = [[] for i in range(10)]
    for i in range(nbrInitial):
        clusters[int(mnist.train_labels[i])].append(mnist.train_imgs[i])

        # K-means
    print("K-means")
    Kmeans = kmeans.Kmeans(clusters)

    # Distance quadratique
    t = time.time()
    n = 0
    for k in range(nbrTester):
        if Kmeans.evaluate(mnist.test_imgs[k], "quadratic") == mnist.test_labels[k]:
            n += 1
    resultat = n / nbrTester * 100
    print("Distance Quadratique: {} % ({})".format(resultat, time.time() - t))
    # Distance moyenne
    t = time.time()
    n = 0
    for k in range(nbrTester):
        if Kmeans.evaluate(mnist.test_imgs[k], "mean") == mnist.test_labels[k]:
            n += 1
    resultat = n / nbrTester * 100
    print("Distance Moyenne: {} % ({})".format(resultat, time.time() - t))

    # K-Neighbors
    print("K-Neighbors")
    Kneighbors = kNeighbors.KNeighbors(clusters, 4)
    # Distance quadratique
    t = time.time()
    n = 0
    for k in range(nbrTester):
        if Kneighbors.evaluate(mnist.test_imgs[k], "quadratic") == mnist.test_labels[k]:
            n += 1
    resultat = n / nbrTester * 100
    print("Distance Quadratique: {} % ({})".format(resultat, time.time() - t))
    # Distance moyenne
    t = time.time()
    n = 0
    for k in range(nbrTester):
        if Kneighbors.evaluate(mnist.test_imgs[k], "mean") == mnist.test_labels[k]:
            n += 1
    resultat = n / nbrTester * 100
    print("Distance Moyenne: {} % ({})".format(resultat, time.time() - t))


## Simple ND
if BDDs["simpleND"]:
    print("Comparaison des algorithmes de clustering sur le MNIST")

    nbr = 1000
    nbrClusters = 3
    nbrTester = 100
    dimOrigine = 4
    scaleNormale = 0.1
    nbrPlusProchesVoisins = 5

    # Cluster d'initialisation
    clusters = [[] for i in range(nbrClusters)]
    (
        pointsND,
        points2D,
        base,
        labels,
        pointsTestsND,
        pointsTests2D,
        labelsTests,
    ) = simpleND.genererSimpleND(nbr, nbrClusters, nbrTester, dimOrigine, scaleNormale)
    for i in range(len(pointsND)):
        clusters[labels[i]].append(pointsND[i])

        # K-means
    print("K-means")
    Kmeans = kmeans.Kmeans(clusters)

    # Distance quadratique
    t = time.time()
    n = 0
    for k in range(nbrTester):
        if Kmeans.evaluate(pointsTestsND[k], "quadratic") == labelsTests[k]:
            n += 1
    resultat = n / nbrTester * 100
    print("Distance Quadratique: {} % ({})".format(resultat, time.time() - t))
    # Distance moyenne
    t = time.time()
    n = 0
    for k in range(nbrTester):
        if Kmeans.evaluate(pointsTestsND[k], "mean") == labelsTests[k]:
            n += 1
    resultat = n / nbrTester * 100
    print("Distance Moyenne: {} % ({})".format(resultat, time.time() - t))

    # K-Neighbors
    print("K-Neighbors")
    Kneighbors = kNeighbors.KNeighbors(clusters, nbrPlusProchesVoisins)

    # Distance quadratique
    t = time.time()
    n = 0
    for k in range(nbrTester):
        if Kneighbors.evaluate(pointsTestsND[k], "quadratic") == labelsTests[k]:
            n += 1
    resultat = n / nbrTester * 100
    print("Distance Quadratique: {} % ({})".format(resultat, time.time() - t))
    # Distance moyenne
    t = time.time()
    n = 0
    for k in range(nbrTester):
        if Kneighbors.evaluate(pointsTestsND[k], "mean") == labelsTests[k]:
            n += 1
    resultat = n / nbrTester * 100
    print("Distance Moyenne: {} % ({})".format(resultat, time.time() - t))
