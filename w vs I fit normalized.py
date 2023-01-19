# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 12:04:57 2022

@author: mrsag

2D Doppler data processing code
"""
############################################################################################################
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as fit
############################################################################################################


timedelay=0
filenumber=132
file=[]
lw=5



############################################################################################################

def Gauss(x,a,b,x0):
    y=np.exp(-b*(x-x0)**2)
    return y

def Gaussfit(w,I):
    xdata=np.asarray(w[minval:maxval])
    ydata=np.asarray(I[minval:maxval])

    ymax_index=(list(ydata)).index(max(ydata))
    xmax_val=xdata[int(len(xdata)/2)]
    xdata=xdata-xmax_val
    #ymin_val=min(ydata)
    ymin_val=np.average(I[100:500])
    ydata=ydata-ymin_val
    ydata=ydata/max(ydata)
    
    parameters, covariance = fit(Gauss, xdata, ydata,maxfev=100000)
    
    fit_y = Gauss(xdata, *parameters)
    fit_y=fit_y+ymin_val
    offset=fit_y[0]-ydata[0]
    fit_y=fit_y-offset
    
    xdata=xdata+xmax_val
    fit_y=np.asarray(fit_y)
    
    return xdata,fit_y,parameters
    


for i in range(132):
    file.append(i+1)

minval=1800            # peak=[1800:1970]
maxval=1970            # len(w)=3648
#print(maxval)
'''
sp1_fit=[]
sp2_fit=[]
sp3_fit=[]
sp4_fit=[]
sp5_fit=[]
sp6_fit=[]
sp7_fit=[]
sp8_fit=[]
sp9_fit=[]
sp10_fit=[]
sp11_fit=[]
sp12_fit=[]
sp13_fit=[]
sp14_fit=[]
sp15_fit=[]
sp16_fit=[]
'''

spec_fit=[]
for i in range(16):
    spec_fit.append([])


# MAIN LOOP
for i in range(1):
    if(file[i]<10):
        f=open("D:\\python files\\2d doppler new\\Data\\0%d.txt"% (file[i]))  # read the data
    if(file[i]>=10):
        f=open("D:\\python files\\2d doppler new\\Data\\%d.txt"% (file[i]))  # read the data
        
    r=np.loadtxt(f)  #load text from that file
    
    # Spectrometer 1
    w1=np.asarray(r[:,0])
    I1=np.asarray(r[:,1])
    
    
    # Spectrometer 2
    w2=np.asarray(r[:,2])
    I2=np.asarray(r[:,3])
    
    # Spectrometer 3
    w3=np.asarray(r[:,4])
    I3=np.asarray(r[:,5])
    
    # Spectrometer 4
    w4=np.asarray(r[:,6])
    I4=np.asarray(r[:,7])
    
    # Spectrometer 5
    w5=np.asarray(r[:,8])
    I5=np.asarray(r[:,9])
    
    # Spectrometer 6
    w6=np.asarray(r[:,10])
    I6=np.asarray(r[:,11])
    
    # Spectrometer 7
    w7=np.asarray(r[:,12])
    I7=np.asarray(r[:,13])
    
    # Spectrometer 8
    w8=np.asarray(r[:,14])
    I8=np.asarray(r[:,15])
    
    # Spectrometer 9
    w9=np.asarray(r[:,16])
    I9=np.asarray(r[:,17])
    
    # Spectrometer 10
    w10=np.asarray(r[:,18])
    I10=np.asarray(r[:,19])
    
    # Spectrometer 11
    w11=np.asarray(r[:,20])
    I11=np.asarray(r[:,21])
    
    # Spectrometer 12
    w12=np.asarray(r[:,22])
    I12=np.asarray(r[:,23])
    
    # Spectrometer 13
    w13=np.asarray(r[:,24])
    I13=np.asarray(r[:,25])
    
    # Spectrometer 14
    w14=np.asarray(r[:,26])
    I14=np.asarray(r[:,27])
    
    # Spectrometer 15
    w15=np.asarray(r[:,28])
    I15=np.asarray(r[:,29])
    
    # Spectrometer 16
    w16=np.asarray(r[:,30])
    I16=np.asarray(r[:,31])
    
    
    #putting all negative error values at zero
    for j in range(len(w1)):
        if(I1[j]<0):
            I1[j]=0
        
        if(I2[j]<0):
            I1[j]=0
            
        if(I3[j]<0):
            I1[j]=0
            
        if(I4[j]<0):
            I1[j]=0
        
        if(I5[j]<0):
            I1[j]=0
        
        if(I6[j]<0):
            I1[j]=0
        
        if(I7[j]<0):
            I1[j]=0
        
        if(I8[j]<0):
            I1[j]=0
        
        if(I9[j]<0):
            I1[j]=0
        
        if(I10[j]<0):
            I1[j]=0
        
        if(I11[j]<0):
            I1[j]=0
        
        if(I12[j]<0):
            I1[j]=0
        
        if(I13[j]<0):
            I1[j]=0
        
        if(I14[j]<0):
            I1[j]=0
        
        if(I15[j]<0):
            I1[j]=0
        
        if(I16[j]<0):
            I1[j]=0
        
        
        
    
    plt.figure(figsize=(40,28))  
    plt.title("Filenumber %d"%file[i],size=75,fontname="cursive",fontweight="bold",color='green')
    
    
    
    # PRINTING THE GAUSSIAN FIT
    
    #s1
    if(max(I1[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w1,I1)
        plt.plot(w1[minval:maxval],I1[minval:maxval]/max(I1[minval:maxval]),label='s1',linewidth=lw) 
        plt.plot(xdata,fit_y,'-',label='fit s1',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp1_fit.append(x_Imax_val)
            spec_fit[0].append(x_Imax_val)
    
    
    #s2
    if(max(I2[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w2,I2)
        plt.plot(w2[minval:maxval],I2[minval:maxval]/max(I2[minval:maxval]),label='s2',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s2',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp2_fit.append(x_Imax_val)
            spec_fit[1].append(x_Imax_val)
    
    #s3
    if(max(I3[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w3,I3)
        plt.plot(w3[minval:maxval],I3[minval:maxval]/max(I3[minval:maxval]),label='s3',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s3',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp3_fit.append(x_Imax_val)
            spec_fit[2].append(x_Imax_val)
    
    #s4
    if(max(I4[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w4,I4)
        plt.plot(w4[minval:maxval],I4[minval:maxval]/max(I4[minval:maxval]),label='s4',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s4',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp4_fit.append(x_Imax_val)
            spec_fit[3].append(x_Imax_val)
    
    #s5
    if(max(I5[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w5,I5)
        plt.plot(w5[minval:maxval],I5[minval:maxval]/max(I5[minval:maxval]),label='s5',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s5',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp5_fit.append(x_Imax_val)
            spec_fit[4].append(x_Imax_val)
    
    #s6
    if(max(I6[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w6,I6)
        plt.plot(w6[minval:maxval],I6[minval:maxval]/max(I6[minval:maxval]),label='s6',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s6',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp6_fit.append(x_Imax_val)
            spec_fit[5].append(x_Imax_val)
    
    #s7
    if(max(I7[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w7,I7)
        plt.plot(w7[minval:maxval],I7[minval:maxval]/max(I7[minval:maxval]),label='s7',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s7',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp7_fit.append(x_Imax_val)
            spec_fit[6].append(x_Imax_val)
    
    #s8
    if(max(I8[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w8,I8)
        plt.plot(w8[minval:maxval],I8[minval:maxval]/max(I8[minval:maxval]),label='s8',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s8',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp8_fit.append(x_Imax_val)
            spec_fit[7].append(x_Imax_val)
    
    #s9
    if(max(I9[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w9,I9)
        plt.plot(w9[minval:maxval],I9[minval:maxval]/max(I9[minval:maxval]),label='s9',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s9',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp9_fit.append(x_Imax_val)
            spec_fit[8].append(x_Imax_val)
    
    #s10
    if(max(I10[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w10,I10)
        plt.plot(w10[minval:maxval],I10[minval:maxval]/max(I10[minval:maxval]),label='s10',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s10',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp10_fit.append(x_Imax_val)
            spec_fit[9].append(x_Imax_val)
    
    #s11
    if(max(I11[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w11,I11)
        plt.plot(w11[minval:maxval],I11[minval:maxval]/max(I11[minval:maxval]),label='s11',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s11',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp11_fit.append(x_Imax_val)
            spec_fit[10].append(x_Imax_val)
    
    #s12
    if(max(I12[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w12,I12)
        plt.plot(w12[minval:maxval],I12[minval:maxval]/max(I12[minval:maxval]),label='s12',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s12',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp12_fit.append(x_Imax_val)
            spec_fit[11].append(x_Imax_val)
    
    #s13
    if(max(I13[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w13,I13)
        plt.plot(w13[minval:maxval],I13[minval:maxval]/max(I13[minval:maxval]),label='s13',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s13',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp13_fit.append(x_Imax_val)
            spec_fit[12].append(x_Imax_val)
    
    #s14
    if(max(I14[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w14,I14)
        plt.plot(w14[minval:maxval],I14[minval:maxval]/max(I14[minval:maxval]),label='s14',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s14',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp14_fit.append(x_Imax_val)
            spec_fit[13].append(x_Imax_val)
        
    #s15
    if(max(I15[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w15,I15)
        plt.plot(w15[minval:maxval],I15[minval:maxval]/max(I15[minval:maxval]),label='s15',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s15',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp15_fit.append(x_Imax_val)
            spec_fit[14].append(x_Imax_val)
    
    #s16
    if(max(I16[minval:maxval])>800):
        xdata,fit_y,p= Gaussfit(w16,I16)
        plt.plot(w16[minval:maxval],I16[minval:maxval]/max(I16[minval:maxval]),label='s16',linewidth=lw)
        plt.plot(xdata,fit_y,'-',label='fit s16',linewidth=lw)
        if(p[1]>0):
            Imax=max(fit_y)
            I_index_imax=(list(fit_y)).index(Imax)
            x_Imax_val=xdata[I_index_imax]
            #sp16_fit.append(x_Imax_val)
            spec_fit[15].append(x_Imax_val)
    
    
    
    
    
    plt.xlabel("Wavelength (nm)",fontname="Times New Roman",fontweight="light",fontsize=60)
    plt.ylabel("Intensity (arb unit)",fontname="Times New Roman",fontweight="light",fontsize=60)
    plt.xticks(fontsize=45,color='purple')
    plt.yticks(fontsize=45,color='purple')
    plt.legend(fontsize=45)
    plt.grid()
    plt.show()
    
'''    
sp_fit=[]
sp_fit.append(sp1_fit)
sp_fit.append(sp2_fit)
sp_fit.append(sp3_fit)
sp_fit.append(sp4_fit)
sp_fit.append(sp5_fit)
sp_fit.append(sp6_fit)
sp_fit.append(sp7_fit)
sp_fit.append(sp8_fit)
sp_fit.append(sp9_fit)
sp_fit.append(sp10_fit)
sp_fit.append(sp11_fit)
sp_fit.append(sp12_fit)
sp_fit.append(sp13_fit)
sp_fit.append(sp14_fit)
sp_fit.append(sp15_fit)
sp_fit.append(sp16_fit)

for i in range(16):
    delay=np.arange(len(sp_fit[i]))
    print("\n\n",sp_fit[i])
    plt.title("Spectrometer: %d"%(1+i))
    plt.plot(delay,sp_fit[i],'ko-')
    plt.show()
'''

'''
for i in range(16):
    delay=np.arange(len(spec_fit[i]))
    print("\n\n",spec_fit[i])
    plt.title("Spectrometer: %d"%(1+i))
    plt.plot(delay,spec_fit[i],'ro-')
    plt.show()
'''