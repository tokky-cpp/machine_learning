<<<<<<< HEAD
#!coding:utf-8
# CRP(中華料理店過程)に基づいてクラス数未定のクラスタリングのための事前分布を決定する。


import random

alpha = 1
n = 100

def crp(alpha=alpha,n=n):
    s=[]
    table={}
=======
#coding=utf:8
import random

def crp(alpha,n): #alpha:パラメータ n:全体の人数
    s=[] #各人が座るテーブル番号のリスト
    table={} #テーブルごとの人数の辞書
>>>>>>> bd344935dfa2787b7f5091ecb6f744335e3d1869
    for i in range(n):
        if(i==0): #1人目だったら無条件に0番目のテーブルに着席
            s.append(0)
            table.setdefault(0,1)
            continue
        
        else:
            prob = random.random() #0-1の範囲
            sum = 0.0 #各テーブルの着席確率を累積していって、probを超えたら着席

            #新規テーブルに対して
            new_p = float(alpha)/(i-1+alpha) 
            sum += new_p

            if(sum>=prob): 
                s.append(len(table))
                table.setdefault(len(table),1)
                continue

            #既存テーブルに対して
            for t in table.keys(): 
                sit_p = float(table[t])/(i-1+alpha)
                sum += sit_p

                if(sum>=prob):
                    s.append(t)
                    table[t] += 1
                    break
                
    return s,table
