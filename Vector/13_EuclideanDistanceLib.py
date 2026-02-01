import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics.pairwise import euclidean_distances

iris = load_iris()
X = iris.data
x1 = X[0].reshape(1,-1)
x2 = X[1].reshape(1,-1)

distance = euclidean_distances(x1,x2)
print("Euclidean Distance ",distance[0][0])