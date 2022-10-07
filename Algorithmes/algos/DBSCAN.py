#
#
#   Algorithme DBSCAN pour le clustering
#
#
import numpy as np
import algos.functions as fct


class DBSCAN:
    def __init__(self, distance):
        """
        Initialise the algorithm
        Nothing to do in fact
        """
        pass

    def evaluate(self, points, eps, minPts, distance):
        """
        Function that use the DBSCAN algorithm in order to predict
        what are the clusters given an number of points

        Inputs:
            points: a list of points
            eps: epsilon (the max distance to be considered neighbors
            minPts: Number minimum of points for one cluster
        Outputs:
            clusters: a list of clusters (indices of the points)

        """

        def epsilonVoisinage(points, i, eps):
            liste = []
            point = points[i]
            for j in range(len(points)):
                d = distance(points[j], point)
                if d < eps and d < 10**-10:
                    liste.append(j)
            return liste

        def etendreCluster(points, i, clusters, ptsVoisins, eps, minPts):
            clusters[-1].append(i)
            for j in ptsVoisins:
                if visites[j] == False:
                    visites[j] = True
                    nouveauxPtsVoisins = epsilonVoisinage(points, j, eps)
                    if len(nouveauxPtsVoisins) >= minPts:
                        ptsVoisins = fct.fusionner(ptsVoisins, nouveauxPtsVoisins)
                inACluster = False
                for cluster in clusters:
                    if j in cluster:
                        inACluster = True
                        break
                if inACluster == False:
                    clusters[-1].append(j)

        clusters = []
        bruit = []
        visites = [False for i in range(len(points))]

        for i in range(len(points)):
            if visites[i] == False:
                point = points[i]
                ptsVoisins = epsilonVoisinage(points, i, eps)
                if len(ptsVoisins) < minPts:
                    bruit.append(i)
                else:
                    clusters.append([])
                    etendreCluster(points, i, clusters[-1], ptsVoisins, eps, minPts)
        return clusters


"""
DBSCAN(D, eps, minPts)
   C = 0
   pour chaque point P non visité des données D
      marquer P comme visité
      PtsVoisins = epsilonVoisinage(D, P, eps)
      si tailleDe(PtsVoisins) < MinPts
         marquer P comme BRUIT
      sinon
         C++
         etendreCluster(D, P, PtsVoisins, C, eps, MinPts)

etendreCluster(D, P, PtsVoisins, C, eps, MinPts)
   ajouter P au cluster C
   pour chaque point P' de PtsVoisins
      si P' n'a pas été visité
         marquer P' comme visité
         PtsVoisins' = epsilonVoisinage(D, P', eps)
         si tailleDe(PtsVoisins') >= MinPts
            PtsVoisins = PtsVoisins U PtsVoisins'
      si P' n'est membre d'aucun cluster
         ajouter P' au cluster C

epsilonVoisinage(D, P, eps)
   retourner tous les points de D qui sont à une distance inférieure à epsilon de P
"""
