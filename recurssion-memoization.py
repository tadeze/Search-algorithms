# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 10:18:12 2015
Use of memoization in recurssion algorithm,
Clearly memoization is way to go for fast execution 
@author: Tadeze
"""
def fib(n):
    if(n<1): return 0
    if(n==1): return 1
    return fib(n-2) + fib(n-1)
def calFib(n,memo):
    if memo[n-1]!=-1: return memo[n-1]
    memo[n-1]=calFib(n-2,memo) + calFib(n-1,memo)
    return memo[n-1]
def fibmemo(n):
    memo=[-1]*n
    memo[0:2]=0,1
    return calFib(n,memo)

import timeit
if __name__=="__main__":
   start = timeit.default_timer()
   fib(40)
   stop = timeit.default_timer()
   print stop - start
   print"\n Result from memo \n"
   startf = timeit.default_timer()
   fibmemo(40)
   stopf = timeit.default_timer()
   print stopf - startf 
    
