x = [2,3]
weight = [0.4,1.5]

dot_product = 0
for i in range(len(x)):
    dot_product += x[i] * weight[i]
print(dot_product)