#!coding:utf-8
import sys
import make_data as md

if(len(sys.argv)>1):
    N = sys.argv[1]
    M = sys.argv[2]

    K = md.make_K(N=N,M=M)

else:
    K = md.make_K()

print K
