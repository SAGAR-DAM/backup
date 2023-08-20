# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 11:23:12 2023

@author: sagar
"""
import numpy as np

def f(r1,t1,r2,t2):
    R=r1**(r2*np.cos(t2))*np.exp(-r2*t1*np.sin(t2))
    T=r2*np.sin(t2)*np.log(r1)+r2*t1*np.cos(t2)
    if(T>np.pi):
        T=-(2*np.pi-T)
    elif(T<np.pi):
        T=2*np.pi-abs(T)
    return(R*(np.cos(T)+1j*np.sin(T)))


r1=3
t1=4

r2=3
t2=4

if(abs(t1)<=np.pi and abs(t2)<=np.pi):
    z1=r1*np.exp(1j*t1)
    z2=r2*np.exp(1j*t2)
    print(z1**z2)
    
    print(f(r1,t1,r2,t2))
    
elif(abs(t1>np.pi) and abs(t2)<=np.pi):
    if(t1>np.pi):
        t1=-(2*np.pi-t1)
    elif(t1<np.pi):
        t1=2*np.pi-abs(t1)
    z1=r1*np.exp(1j*t1)
    z2=r2*np.exp(1j*t2)
    print(z1**z2)
    
    print(f(r1,t1,r2,t2))
    
elif(abs(t1<=np.pi) and abs(t2)>np.pi):
    if(t2>np.pi):
        t2=-(2*np.pi-t2)
    elif(t2<np.pi):
        t2=2*np.pi-abs(t2)
    z1=r1*np.exp(1j*t1)
    z2=r2*np.exp(1j*t2)
    print(z1**z2)
    
    print(f(r1,t1,r2,t2))
    
elif(abs(t1)>np.pi and abs(t2)>np.pi):
    if(t1>np.pi):
        t1=-(2*np.pi-t1)
    elif(t1<np.pi):
        t1=2*np.pi-abs(t1)
        
    if(t2>np.pi):
        t2=-(2*np.pi-t2)
    elif(t2<np.pi):
        t2=2*np.pi-abs(t2)
    z1=r1*np.exp(1j*t1)
    z2=r2*np.exp(1j*t2)
    print(z1**z2)
    
    print(f(r1,t1,r2,t2))