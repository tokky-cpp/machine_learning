#!coding:utf-8
# ガウスガンマ分布に基づいてデータ生成
# 生成モデルにおいて、クラスごとのガウス分布のパラメータを決定するために使用

import matplotlib.pyplot as plt
import numpy as np

POINT = 4
a = 5
b = 6
beta = 2
mu0 = 0

def normal_gamma(a=a,b=b,mu0=mu0,beta=beta,POINT=POINT,see=False):

    ll = []
    mumu = []

    for i in range(POINT):
        lamb = np.random.gamma(a,float(1)/b,1)
        ll.append(lamb[0])
        mu = np.random.normal(mu0, float(1)/(beta*lamb))
        mumu.append(mu)
    
    if(see):
        plt.plot(mumu,ll,"o")
        plt.show()
        

    return [(m,l) for (m,l) in zip(mumu,ll)]
