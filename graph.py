#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

def graph(table): #ディクショナリ形式を受け取ってグラフにする
    table = sorted(table.items(),key=lambda x: x[1])
    table.reverse()
    print table
    number = []
    people = []
    for (t,n) in table:
        number.append(t)
        people.append(n)
        
    
    x=[i for i in range(len(people))]
    y=people
    
    plt.plot(x,y)
    plt.show()

    return
