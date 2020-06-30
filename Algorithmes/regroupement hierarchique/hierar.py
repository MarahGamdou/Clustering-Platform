import numpy as np
import random as rd
import gzip
import matplotlib.pyplot as plt
##étapes:
# on met donnée / cluster
# afficher /stocker les étapes de fusion////
# N-1 fusions

###Entree
'''Tab_Entree = [rd.randint(0, 100) for i in range(20)]'''
parametre_distance_cluster = input('entrer : max ou min')  ##mean à faire

##Entree images
f = gzip.open('t10k-images-idx3-ubyte.gz','r')

##labels test
g = gzip.open('t10k-labels-idx1-ubyte.gz','r')
g.read(8)
buf = g.read(1000)
labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)


image_size = 28
num_images = 1000
f.read(16)
buf = f.read(image_size * image_size * num_images)
data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
data = data.reshape(num_images, image_size, image_size, 1)
liste_alea=[rd.randint(0,1000) for i in range(50)]
Tab_Entree=[np.asarray(data[liste_alea[i]]).squeeze() for i in range (50)]
labels_expe=[labels[liste_alea[i]] for i in range(50)]


###distance_element
def distance_element(e1, e2):
    return (abs(e1 - e2))

def distance_images(e1,e2):
    dist=0
    for row in range(len(e1)):
        for cell in range(len(e1[row])):
            dist+=(e1[row][cell]-e2[row][cell])**2
    return dist**0.5


###distance_cluster
def distance_cluster(c1, c2):
    if parametre_distance_cluster == 'min':
        min_distance_cluster = distance_images(c1[0], c2[0])
        for element_c1 in c1:
            for element_c2 in c2:
                if distance_images(element_c1, element_c2) < min_distance_cluster:
                    min_distance_cluster = distance_images(element_c1, element_c2)
        return min_distance_cluster
    elif parametre_distance_cluster == 'max':
        max_distance_cluster = distance_images(c1[0], c2[0])
        for element_c1 in c1:
            for element_c2 in c2:
                if distance_images(element_c1, element_c2) > max_distance_cluster:
                    max_distance_cluster = distance_images(element_c1, element_c2)
        return max_distance_cluster
    elif parametre_distance_cluster== 'mean1':
        dist=0
        for element_c1 in c1:
            for element_c2 in c2:
                dist += distance_images(element_c1, element_c2)
        return dist/(len(c1)*len(c2))


###fusion
def fusion(ligne, i):
    c = {}
    for element in range(N):
        if ligne[element] in c.keys():
            c[int(ligne[element])] = c[int(ligne[element])] + [Tab_Entree[element]]
        else:
            c[int(ligne[element])] = [Tab_Entree[element]]
    print(c)

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
    print(ligne_suivante)
    if l==i-1:
        for element_ligne in range(N):
            if ligne[element_ligne]==l:
                ligne_suivante[element_ligne]=j
    else:
        for element_ligne in range(N):
            if ligne[element_ligne]==l:
                ligne_suivante[element_ligne]=j
            elif ligne[element_ligne]==i-1:
                ligne_suivante[element_ligne]=l
    print(ligne_suivante)
    return ligne_suivante


###main
N = len(Tab_Entree)
Tab_similarite = np.zeros((N, N), int)

for i in range(0, N):
    Tab_similarite[0][i] = i

for i in range(N - 1):
    Tab_similarite[i + 1] = fusion(Tab_similarite[i], N - i)

print(Tab_similarite)
k10=Tab_similarite[N-11]

def occu_max(liste):
    l=np.zeros(10)
    for i in liste:
        l[i]+=1
    max_l=max(l)
    for k in range(len(l)):
        if l[k]==max_l:
            return k


def analyse():
    pourc=0
    c={}
    for indice in range(len(k10)):
        if k10[indice] in c.keys():
            c[k10[indice]]+= [labels_expe[indice]]
        else:
            c[k10[indice]]= [labels_expe[indice]]
    for liste in c.values():
        a=occu_max(liste)
        for i in liste :
            if i == a :
                pourc+=1
    return pourc/(len(k10))





