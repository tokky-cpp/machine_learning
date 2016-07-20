import matplotlib.pyplot as plt
import numpy as np

mu = [[-10,10],[10,10],[10,-10],[-10,-10]]
sigma = [[1,1],[1,1],[1,1],[1,1]]

vec = []

for i in range(4):
    x = []
    y = []
    for j in range(5):
        x1 = np.random.normal(mu[i][0],sigma[i][0])
        x.append(x1)

        y1 = np.random.normal(mu[i][1],sigma[i][1])
        y.append(y1)

        vec.append([x1,y1])

    plt.plot(x,y,'o')

plt.show()


gram = []

for i in vec:
    row = []
    for j in vec:
        row.append(np.dot(i,j))
    gram.append(row)

K = np.matrix(gram)

print(K)
        
