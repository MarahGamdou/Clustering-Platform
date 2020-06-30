import numpy as np
from random import randint,random
import matplotlib.pyplot as plt

def normale(scaleNormale,dimOrigine):
    return np.random.normal(scale=scaleNormale,size=(dimOrigine,))

def gramSchmidt(baseOrigine):
    """
    Gram-Schmidt Algorithm that convert a base into an orthonormal base
    """
    baseOrthonormee = []
    for i in range(len(baseOrigine)):
        temp_vec = baseOrigine[i]
        for vecteur in baseOrthonormee:
            temp_vec=temp_vec-np.dot(temp_vec,vecteur)*vecteur
        baseOrthonormee.append(temp_vec/np.dot(temp_vec,temp_vec)**(1/2))
    return baseOrthonormee

def reducDim(points,dimVoulue,base=False):
    """
    Function that take a list of points and a desired dimension and project
    each vector in that space of given dimension
    """
    newPoints=[]
    n=len(points[0])-1
    dim=len(points[0])
    if dimVoulue>dim: return
    if base==False:
        base=[]
        for i in range(n):
            vector=2*np.random.random_sample((n+1,))-1
            base.append(vector)
        base = gramSchmidt(base)
    for i in range(len(points)):
        vector=np.zeros((n,))
        for j in range(n):
            vector[j]=np.dot(base[j],points[i])
        newPoints.append(vector)
    return newPoints,base
    
def genererSimpleND(nbr=200,nbrClusters=3,nbrTests=50,dimOrigine=4,scaleNormale=0.1):
    """
    Function that generate data (points) in a dim chosen, the projection in 2D
    based on a normal law
    
    Inputs:
        nbr: number of points
        nbrClusters: number of clusters simulated
        dimOrigine: The dimension of the space (when the points are created)
        scaleNormale:  Scale for the normal law
    
    Outputs:
        pointsND: points in the N-dimensionnal space
        points2D: points in the 2D-space (after projection)
        base: base of projection of the points into 2D
        labels: The labels for each points (usefull if supervised learning)
    
    """
    pointsND=[]
    barycentres=[]
    labels=[]
    
    pointsTestsND=[]
    labelsTests=[]
    
    # On crée les barycentres pour les k clusters
    for i in range(nbrClusters):
        barycentres.append(2*np.random.random_sample((dimOrigine,))-1)
    
    # Generation of points to randomly clusters
    for n in range(nbr):
        cluster=randint(0,nbrClusters-1)
        point=barycentres[cluster]+normale(scaleNormale,dimOrigine)
        labels.append(cluster)
        pointsND.append(point)
    points2D,base=reducDim(pointsND,2)  
    
    # Generation of points for the test list to randomly clusters
    for n in range(nbrTests):
        cluster=randint(0,nbrClusters-1)
        point=barycentres[cluster]+normale(scaleNormale,dimOrigine)
        labelsTests.append(cluster)
        pointsTestsND.append(point)
    pointsTests2D,base=reducDim(pointsTestsND,2,base)
    
    
    return pointsND,points2D,base,labels,pointsTestsND,pointsTests2D,labelsTests