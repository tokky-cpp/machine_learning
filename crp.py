#!coding:utf-8
# CRP(中華料理店過程)に基づいてクラス数未定のクラスタリングのための事前分布を決定する。


import random

alpha = 1
n = 100

def crp(alpha=alpha,n=n):
    s=[]
    table={}
    for i in range(n):
        if(i==0): #1人目だったら0番目のテーブルに着席
            s.append(0)
            table.setdefault(0,1)
            continue
        
        else:
            prob = random.random() #0-1の範囲
            sum = 0.0 #各テーブルの着席確率を累積していって、probを超えたら着席
            #新規テーブルの着席確率
            new_p = float(alpha)/(i-1+alpha) 
            sum += new_p

            if(sum>=prob): 
                s.append(len(table))
                table.setdefault(len(table),1)
                continue

            #既存テーブルへの着席確率を見ていく
            for t in table.keys(): 
                sit_p = float(table[t])/(i-1+alpha)
                sum += sit_p

                if(sum>=prob):
                    s.append(t)
                    table[t] += 1
#                    print i,"sit",t
                    break
                
    return s,table
                
    
