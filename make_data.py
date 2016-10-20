#!coding:utf-8
# 生成モデルに基づいた特徴ベクトル生成
# 特徴ベクトル間の類似度K(行列)を生成

import crp
import normal_gamma
import matplotlib.pyplot as plt
import numpy as np

N = 5 # data points
M = 8 # dimension of data
alpha = 1.0 # palameter for CRP
a = 5 # palameter for normal_gamma distribution
b = 10 # palameter for normal_gamma distribution

#クラスの事前分布(CRP)
(s,table) = crp.crp(alpha,N)
cls_num = len(table)
print cls_num,"clusters"

#パラメータの事前分布(ガウスガンマ分布)
theta = normal_gamma.normal_gamma(POINT = cls_num,see=False)

#data = [] #データ点
data = np.empty((0,M))

#ガウス分布に基づいてデータ点生成
for i in s: #全データに対して
    d = []
    for j in range(M): #次元数分だけデータを生成
        d.append(np.random.normal(theta[i][0],theta[i][1]))
    data = np.append(data, np.array([d]), axis=0)
#    data.append(d)

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




print data
print len(data)

plt.show()

print("--------類似度計算-------")

K = np.empty((0,N))
for i in range(N):
    ker = []
    for j in range(N):
        ker.append(data[i].dot(data[j]))

    K = np.append(K, np.array([ker]), axis=0)

print K
