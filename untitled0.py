# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:38:35 2022

@author: mrsag
"""
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import os
import numba

T=[387.75409,381.19788,378.22202,394.04990,387.28772,384.21942,398.30597,391.40289,387.90717,401.54333,394.53220,391.35223]
beta=[0.6,1.0,1.4,1.8]
T_0_2=[T[0],T[3],T[6],T[9]]
T_0_6=[T[1],T[4],T[7],T[10]]
T_1_0=[T[2],T[5],T[8],T[11]]
print(len(beta))
plt.figure(figsize = (34,20))
plt.title('Plot of \u03B2 vs T$_m$',size=75,fontname="cursive",fontweight="bold",color='green')
plt.plot(beta,T_0_2,'r-o',label=r'f$_r$=0.2',linewidth=5,markersize=20)
plt.plot(beta,T_0_6,'g--X',label='f$_r$=0.6',linewidth=5,markersize=25)
plt.plot(beta,T_1_0,'k-X',label='f$_r$=1.0',linewidth=5,markersize=20)
plt.xlabel("\u03B2 (K/sec)" ,fontname="Times New Roman",fontweight="light",fontsize=60)
plt.ylabel('T$_m$(K)',fontname="Times New Roman",fontweight="light",fontsize=60)
plt.legend()
plt.grid()
plt.xticks(fontsize=45)
plt.yticks(fontsize=45)
plt.legend(fontsize=45)
plt.show()