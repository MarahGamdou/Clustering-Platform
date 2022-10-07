#
#
#   Algorithme K-means pour le clustering
#
#
import numpy as np
import algos.functions as fct


class Kmeans:
    def __init__(self, clusters):
        """
        Initialise the clusters
        Input:
            clusters: list of lists of clusters
        Output:
            None
            (Create the k value, and the center of each cluster
        """
        self.k = len(clusters)  # Value of k
        self.centers = []  # Center of each cluster

        # Création des milieux des clusters
        for cluster in clusters:
            center = np.zeros(cluster[0].shape)
            for element in cluster:
                center += element
            center = center / len(cluster)
            self.centers.append(center)

    def evaluate(self, entree, nomDistance="quadratic"):
        if (
            False
        ):  # Servira pour prendre en entrée non pas un seul élément, mais une multitude
            # Il faut juste mettre la bonne condition
            resultats = []
            for x in X:
                resultat.append(self.evaluate(x, nomDistance))
            return resultats
        else:
            # Evaluate the output for an X
            distmin = np.inf
            bestcluster = 0

            if nomDistance == "quadratic":
                distance = fct.distance_quadratic
            elif nomDistance == "mean":
                distance = fct.distance_mean
            else:
                distance = fct.distance_mean

            for i in range(self.k):
                dist = distance(entree, self.centers[i])
                if dist < distmin:
                    distmin = dist
                    bestcluster = i
            return bestcluster
