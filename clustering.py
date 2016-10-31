#!coding:utf-8
#崩壊型ギブスサンプリング(続・パタp264)に基づいて記述

import numpy as np
from math import log
import math
import crp


def cut(A,i): #行列Aからi行目i列目の要素をなくした行列を返す i=(0,…,N-1)
    if(A.shape[0]!=A.shape[1]):
        print("[Error]正方行列ではありません")
        print(A)
    
    return np.delete(np.delete(A,i,1),i,0)


def clustering(K,M,W,alpha,beta):
    # K : 類似度行列
    # M : 特徴ベクトルの次元数
    # W : (N*N行列)中心化したウィシャート分布の共分散行列の事前分布
    # alpha : 所属クラスを表す潜在変数
    # beta : ナンダコレ？

    N = K.shape[0]
    M = float(M)
    beta = float(beta)

    # Step 1 初期設定 
    s,s_i = crp.crp(alpha,N) #所属クラスを示す潜在変数を初期化
    c = len(s_i) #総クラス数
    P_max = 0.0 #事後確率の最大値を初期化

    # Step 2 所属クラスの更新
    prob = []
    for i in range(N):
        p = 0.0
        p += -1*(M/2.0)*log(2)
        p += -1*((N-1)/4)*log(math.pi)
        p += -1*log(math.gamma((M-N+1)/2))
        p += ((M+beta)/2)*log((np.linalg.det(K+np.linalg.inv(W)))/(np.linalg.det(cut(K,i)+np.linalg.inv(cut(W,i)))))
        p += -1*(beta/2)*log(np.linalg.det(W)/np.linalg.det(cut(W,i)))
        p += (M-N+1)/2.0*log(np.linalg.det(K)/np.linalg.det(cut(K,i)))
        p += -1*(1/2.0)*log(np.linalg.det(cut(K,i)))
        print i,p
        prob.append(p)


        
        
        
