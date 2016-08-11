#coding=utf:8

import random


def crp(alpha,n): #alpha:パラメータ n:全体の人数
    s=[] #各人が座るテーブル番号のリスト
    table={} #テーブルごとの人数の辞書
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
                
    
