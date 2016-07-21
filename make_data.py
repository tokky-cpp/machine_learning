import crp
import normal_gamma
import matplotlib.pyplot as plt
import numpy as np

N = 100 # data points
M = 2 # dimension of data
alpha = 1.0 
a = 5
b = 10

#クラスの事前分布(CRP)
(s,table) = crp.crp(alpha,N)
print len(table),"clusters"

#パラメータの事前分布(ガウスガンマ分布)
theta = normal_gamma.normal_gamma(a,b,0,2,len(table),False)

data = [] #データ点

#ガウス分布に基づいてデータ点生成
for i in s:
    d = []
    for j in range(M):
        d.append(np.random.normal(theta[i][0],theta[i][1]))
    data.append(d)

# data visualize
for i in range(len(table)):
    x = []
    y = []

    for d in range(len(data)):
        if(s[d]==i):
            x.append(data[d][0])
            y.append(data[d][1])

    plt.plot(x,y,"o")
print(table)
plt.show()
