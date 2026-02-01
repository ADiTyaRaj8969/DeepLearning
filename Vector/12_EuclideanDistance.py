from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
x1 = X[0]
x2 = X[1]
print(x1)
print(x2)
x1 = list(x1)
x2 = list(x2)
sum_sq = 0
for i in range(len(x1)):
    diff = x1[i]-x2[i]
    sum_sq += diff ** 2
distance = sum_sq ** 0.5
print(distance)