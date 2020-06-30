#
#
#   Algorithme Regroupement Hiérarchique pour le clustering
#
#
import numpy as np
import algos.functions as fct


class RegroupementHierarchique:
    def __init__(self,Tab_Entree,parametre_distance_cluster='min'):
        self.N = len(Tab_Entree)
        self.Tab_similarite = np.zeros((self.N, self.N), int)

        if parametre_distance_cluster=="min":
            distance_cluster=fct.distance_cluster_min
        elif parametre_distance_cluster=="max":
            distance_cluster=fct.distance_cluster_max
        elif parametre_distance_cluster=="mean":
            distance_cluster=fct.distance_cluster_mean
        else:
            distance_cluster=fct.distance_cluster_min

        
        def fusion(ligne, i):
            c = {}
            for element in range(self.N):
                if ligne[element] in c.keys():
                    c[int(ligne[element])] = c[int(ligne[element])] + [Tab_Entree[element]]
                else:
                    c[int(ligne[element])] = [Tab_Entree[element]]

            min = distance_cluster(c[0], c[1])
            indices_min = (0, 1)
            for j in range(i-1):
                for l in range(j + 1, i):
                    if distance_cluster(c[j], c[l]) < min:
                        min = distance_cluster(c[j], c[l])
                        indices_min = (j, l)
            j,l = indices_min
            #on a assuré j<l
            ligne_suivante = ligne
            if l==i-1:
                for element_ligne in range(self.N):
                    if ligne[element_ligne]==l:
                        ligne_suivante[element_ligne]=j
            else:
                for element_ligne in range(self.N):
                    if ligne[element_ligne]==l:
                        ligne_suivante[element_ligne]=j
                    elif ligne[element_ligne]==i-1:
                        ligne_suivante[element_ligne]=l
            return ligne_suivante

        for i in range(self.N):
            self.Tab_similarite[0][i] = i

        for i in range(self.N - 1):
            print(i/self.N)
            self.Tab_similarite[i + 1] = fusion(self.Tab_similarite[i], self.N - i)

    def evaluate(self,k):
        return self.Tab_similarite[self.N-1-k]
