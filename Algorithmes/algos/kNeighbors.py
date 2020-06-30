#
#
#   Algorithme K-Neighbors pour le clustering
#
#
import numpy as np
import algos.functions as fct


class KNeighbors:
    def __init__(self,clusters,k=3):
        """
        Initialise the clusters
        Input:
            clusters: list of lists of clusters
        Output:
            None
            Only store that list of lists
        """
        self.k=k                     #Value of k
        self.clusters=clusters       #Values of points


    def evaluate(self, entree, nomDistance="quadratic"):
        if False: #Servira pour prendre en entrée non pas un seul élément, mais une multitude
                  #Il faut juste mettre la bonne condition
            resultats=[]
            for x in X:
                resultat.append(self.evaluate(x,nomDistance))
            return resultats
        else:
            #Evaluate the output for an X

            if nomDistance =="quadratic":
                distance = fct.distance_quadratic
            elif nomDistance == "mean":
                distance = fct.distance_mean
            else:
                distance = fct.distance_mean

            elements=[] #Liste des couples [distance,cluster]
            for i in range(len(self.clusters)):
                cluster=self.clusters[i]
                for vector in cluster:
                    elements.append([distance(vector,entree),i])
            elements=fct.trier(elements,lambda x,y:x[0]<y[0])

            resultat=np.zeros((self.k,))
            for k in range(self.k):
                resultat[elements[k][1]]+=1
            return np.array(resultat).argmax()
