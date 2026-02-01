from sklearn.datasets import load_iris
import numpy as np
iris = load_iris()
X = iris.data
y = iris.target
print(X.shape)
x = X[0]
print(x)
w = np.array([0.2,0.4,0.6,0.8])
b = 0.5
dot_product = x @ w + b
print(dot_product)
relu_output = max(0, dot_product)
print(relu_output)
for i in range(5):
    x = X[i]
    y_out = (w @ x) + b
    print(f"Sample: {i} output:", y_out)