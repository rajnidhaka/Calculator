# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 18:40:35 2022

@author: hp
"""
g
g=True
while g==True:
    print("do you want to repeat calculator?")
    h=input("y for yes, n for no:")
    if h == "y":
        x=int(input("Enter 1st number:"))
        y=int(input("Enter 2nd number:"))
        
        e=True
        while e==True:
            
            z=input("Enter the operation, s for sum , st for subtraction, m for multiplication ,d for division:")  
            a=x+y
            b=x-y
            c=x*y
            if z=="s":
                print(a)
                e=False
            elif z=="st":
                print(b)
                e=False
            elif z=="m" :
                print(c)
                e=False
            elif z=="d":
                if y==0:
                    print("denominator is zero")
                    break
                else:
                    d=x/y
                    print(d)
                    e=False
            else:
                print("its not valid opration like s,st,m,d")
    elif h=="n": 
        g=False
    else:
        print("its neither y nor n")
                
              
   
        
        
