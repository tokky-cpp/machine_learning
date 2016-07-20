import matplotlib.pyplot as plt
import numpy as np

POINT = 4
a = 5
b = 6
beta = 2
mu0 = 0

ll = []
mumu = []

for i in range(POINT):
    lamb = np.random.gamma(a,float(1)/b,1)
    ll.append(lamb)
    mu = np.random.normal(mu0, float(1)/(beta*lamb))
    mumu.append(mu)

plt.plot(mumu,ll,"o")
plt.show()
