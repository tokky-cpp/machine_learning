#!coding:utf-8

# 一発で計算できるようにプログラム化

import sys
import make_data as md
import clustering as cls

#------------[start]データ生成〜類似度行列計算----------

if(len(sys.argv)>1): #オプション受け取り
    N = sys.argv[1] # N:個体数
    M = sys.argv[2] # M:個体の特徴ベクトルの次元

    K = md.make_K(N=N,M=M) # 特徴ベクトル生成->類似度行列生成

else:
    K = md.make_K() #オプションがなければデフォルト値(N=5,M=?)で類似度行列生成

print K
#------------[end]データ生成〜類似度行列計算----------

#------------クラスタリング----------

#clustering(N,M,W,alpha,beta) # 類似度行列とその他のパラメータが与えられたもとで崩壊型ギブスサンプリングを行う


M=5
cls.clustering(K=K,M=M,W=K,alpha=1,beta=2)
