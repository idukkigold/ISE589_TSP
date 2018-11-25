from sklearn.decomposition import PCA
from scipy.spatial import distance
import numpy as np

C=[[0,3,4,6,8,9,8,10],
   [3,0,5,4,8,6,12,8],
   [4,5,0,2,2,3,5,7],
   [6,4,2,0,3,2,5,4],
   [8,8,2,3,0,2,2,4],
   [9,6,3,2,2,0,3,2],
   [8,12,5,5,2,3,0,2],
   [10,9,7,4,4,2,2,0]]

pca = PCA(n_components=2)
X3d = pca.fit_transform(C)
X3d=np.random.RandomState(42).rand(30,2)
for
np.random.shuffle(X3d)
X3d=list(X3d)

for i,city in enumerate(X3d):
    city.append(i)

Tour=[(X3d[-1])]
NotinTour=list(X3d[:-1])
k=0
print("Tour: ",Tour)
print("Not in Tour: ",NotinTour)
n=len(NotinTour)+1

def findNextCity():
    global NotinTour,k_city,addcity,j,j_city
    d_min = 100

    for j,Tx in enumerate(Tour):
        # print("j tx",j,Tx)
        for k, Nx in enumerate(NotinTour):
            # print("k,Nx",k,Nx)

            d=distance.euclidean(Tx,Nx)
            # print(d)
            if (d<d_min):
                j_city=j
                d_min=d
                k_city=k
                addcity=Nx



    NotinTour = NotinTour[0:k_city] + NotinTour[k_city + 1:]
    return addcity

from timeit import default_timer as timer

start = timer()
# ...

while n>0:
    print("Tour: ", Tour)
    print("Not in Tour: ",NotinTour)
    k = findNextCity()
    Tour=Tour[0:j_city]+[k]+Tour[j_city:]
    print(Tour)
    n-=1

print("Final:",Tour)


end = timer()
print(end - start)