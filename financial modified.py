"""
Created on Wed Jun  1 06:48:51 2022
@author: SAGAR DAM
FINANCIAL CALCULATOR
"""


'''
Description:: 
____________

This code takes some input in the format of array of the past net profits and 
cash flows (yearly basis) and w.r.t each year's performance and calculates the average 
increament of NP of CF (CAGR or Average, whichever is lower), calculates the future NP's 
and CF's for next (typically 40) years. While calculating the next year's performances, 
the code halfs the increament rate after every 5 future years and finally takes same for 
all the way from 20th to 40th year. So for the input of the profits of last 10years, it
will generate 10 forecasts for any future year's profit and take the average of them and
discount them to current value. According to that, it will use the DCF methode to evaluate
the intrinsic share price of the company. 

'''
#######################################################
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import os
import numba
#######################################################
'''               INPUT  PANEL                      '''
#######################################################

current_price=2788                   #current market price
marketcap=267405                      #market cap of the company
debt_to_equity=0.13                    #debt_to equity
roce=29.7                              #ROCE
roe=23.2                             #ROE
pe=70                              #pe ratio of the company
medpe=58                             #avg pe of 10Y
pb=19                              #PB
medpb=15.4                          #avg pb of 10y
peg=7.21                            #PEG
inflation=7                         #assumed inflation rate
margin_of_safety=20                    #margin of safety


netprofit=[881,1021,1160,1263,1427,1803,2016,2098,2208,2774,3207,3085]
cashflow=[762,710,1187,1402,1188,2243,1527,2113,2470,3038,3683,986]


company="ASIAN PAINTS"

factor=2
time=40
starting_year=2011

current_year=2023


#######################################################
'''           Calculation by NP Panel               '''
#######################################################

incrementnp=[]                         #rates of NP change
fut_np=[]                              #future NP s
current_value_of_fut_np=0              #current value of total future NPs



#calculation for the average rate of increase of NP
for i in range(len(netprofit)-1):
    if(netprofit[i]>0 and netprofit[i+1]>0):
        inc=(netprofit[i+1]-netprofit[i])*100/netprofit[i]
        incrementnp.append(inc)
    elif(netprofit[i]>0 and netprofit[i+1]<0):
        inc=(netprofit[i+1]-netprofit[i])*100/netprofit[i]
        incrementnp.append(inc)
    elif(netprofit[i]<0 and netprofit[i+1]>0):
        inc=(netprofit[i+1]-netprofit[i])*100/netprofit[i+1]
        incrementnp.append(0)
    elif(netprofit[i]<0 and netprofit[i+1]<0):
        if(netprofit[i+1]<netprofit[i]):
            inc=-(netprofit[i+1]-netprofit[i])*100/netprofit[i]
            incrementnp.append(inc)
        elif(netprofit[i+1]>netprofit[i]):
            inc=(netprofit[i+1]-netprofit[i])*100/netprofit[i]
            incrementnp.append(0)
        
avg_inc_np=np.mean(incrementnp)       #mean value of rate of increase of NPs
stdev_inc_np=np.std(incrementnp)      #Standard deviation of increament of NPs


#decimal rate of NP increament
if(netprofit[len(netprofit)-1]>0 and netprofit[0]>0):
    cagrnp=((netprofit[len(netprofit)-1]/netprofit[0])**(1/(len(netprofit)-1))-1)*100    
    cagrnp_binval=True
    if(avg_inc_np<cagrnp):
        r=1+avg_inc_np/(factor*100) 
        absolute_inc_rate_NP= 1+avg_inc_np/100                  
    else:
        r=1+cagrnp/(factor*100)
        absolute_inc_rate_NP= 1+cagrnp/100                  

else:
    r=1+avg_inc_np/(factor*100)
    absolute_inc_rate_NP= 1+avg_inc_np/100                  

#absolute_inc_rate_NP=(1+absolute_inc_rate_NP)/2     #To even reduce the future NP projections in given years.
#print(incrementnp)

#calculation for the future net profits in 2d array
future_np_matrix=[]
if(r>0):
    for i in range(time):
        if(i<5): #assuming the rate same for first 5 years
            future_np_array=[]     #determines future np's w.r.t previous all years by proper rate
            for j in range(len(netprofit)):       #to calculate the future net profits of future i'th year  w.r.t till this year + this to (i-1)th year
                value=(netprofit[j])*(absolute_inc_rate_NP**(len(netprofit)-(1+j)))*(r**(i+1))      # formula including both contributions
                future_np_array.append(value)
            x=np.mean(future_np_array)
            #x=netprofit[len(netprofit)-1]*r**(i+1)
            future_np_matrix.append(future_np_array)
            fut_np.append(x)
            current_value_of_fut_np=current_value_of_fut_np+x/(1+inflation/100)**(1+i)
        elif(5<=i<10):  #rates taken to be half at next 5 yrs
            r1=(1+r)/2
            future_np_array=[]
            for j in range(len(netprofit)):
                value=(future_np_matrix[-1][j])*r1
                future_np_array.append(value)
            x=np.mean(future_np_array)
            #x=fut_np[len(fut_np)-1]*r1
            future_np_matrix.append(future_np_array)
            fut_np.append(x)
            current_value_of_fut_np=current_value_of_fut_np+x/(1+inflation/100)**(1+i)

        elif(10<=i<15): # again half for next 5 years
            r2=(1+r1)/2
            future_np_array=[]
            for j in range(len(netprofit)):
                value=(future_np_matrix[-1][j])*r2
                future_np_array.append(value)
            x=np.mean(future_np_array)
            #x=fut_np[len(fut_np)-1]*r2
            future_np_matrix.append(future_np_array)
            fut_np.append(x)
            current_value_of_fut_np=current_value_of_fut_np+x/(1+inflation/100)**(1+i)
        elif(15<=i<20):  #again half for next 5 yrs
            r3=(1+r2)/2
            future_np_array=[]
            for j in range(len(netprofit)):
                value=(future_np_matrix[-1][j])*r3
                future_np_array.append(value)
            x=np.mean(future_np_array)
            #x=fut_np[len(fut_np)-1]*r3
            future_np_matrix.append(future_np_array)
            fut_np.append(x)
            current_value_of_fut_np=current_value_of_fut_np+x/(1+inflation/100)**(1+i)

        else:
            r4=(1+(1+r3)/2)/2   # final rate
            #r4=(1+r3)/2
            future_np_array=[]
            for j in range(len(netprofit)):
                value=(future_np_matrix[-1][j])*r1
                future_np_array.append(value)
            x=np.mean(future_np_array)
            #x=fut_np[len(fut_np)-1]*r4
            future_np_matrix.append(future_np_array)
            fut_np.append(x)
            current_value_of_fut_np=current_value_of_fut_np+x/(1+inflation/100)**(1+i)
else:
    for i in range(time):
        future_np_array=[]     #determines future np's w.r.t previous all years by proper rate
        for j in range(len(netprofit)):
            value=(netprofit[j])*r**(len(netprofit)-(1+j)+(i+1))
            future_np_array.append(value)
        x=np.mean(future_np_array)
        #x=netprofit[len(netprofit)-1]*r**(i+1)
        future_np_matrix.append(future_np_array)
        fut_np.append(x)
        current_value_of_fut_np=current_value_of_fut_np+x/(1+inflation/100)**(1+i)
        

all_fut_np=np.sum(np.array(fut_np))                    #sum of all future profits
fut_mcp=marketcap*(1+inflation/100)**40                #future value of todays market cap by inflation
int_val_np=current_value_of_fut_np*current_price/marketcap

print("CALCULATION USING NET PROFIT:")
print("")

print("net profit growths: ",incrementnp)
print("Average increase of net profit till now: ",avg_inc_np)
print("CAGR-NP: ",cagrnp)
print("Future value of today's market cap by ",inflation,"% inflation: ",fut_mcp)
print("Sum of all future net profit: ",all_fut_np)
print("Current share price at intrinsic value: ",int_val_np)
print("Current share price with margin of safety: ",int_val_np*(1-margin_of_safety/100))



print("")
print("")
R=100*(np.array([r,r1,r2,r3,r4])-1)    #Expected future profit growth after 5 yr intervals. Including the factor. 
R = [ '%.2f' % elem for elem in R ]    #r=1+avg_inc_np/(factor*100) ;  r1=(1+r)/2 ; ... so on
#print(R)
print("###################################################################################")
print("###################################################################################")
print("###################################################################################")
print("###################################################################################")
print("")
print("")

##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################

#######################################################
'''           Calculation by CF Panel               '''
#######################################################

incrementcashflow=[]                       #rates for the CF change
fut_cf=[]                                  #cash flows in future
current_value_of_fut_cf=0                  #sum of future cash flows at present


#calculation for the CF increase rates
for i in range(len(cashflow)-1):
    if(cashflow[i]>0 and cashflow[i+1]>0):
        inc=(cashflow[i+1]-cashflow[i])*100/cashflow[i]
        incrementcashflow.append(inc)
    elif(cashflow[i]>0 and cashflow[i+1]<0):
        inc=(cashflow[i+1]-cashflow[i])*100/cashflow[i]
        incrementcashflow.append(inc)
    elif(cashflow[i]<0 and cashflow[i+1]>0):
        inc=(cashflow[i+1]-cashflow[i])*100/cashflow[i+1]
        incrementcashflow.append(0)
    elif(cashflow[i]<0 and cashflow[i+1]<0):
        if(cashflow[i+1]<cashflow[i]):
            inc=-(cashflow[i+1]-cashflow[i])*100/cashflow[i]
            incrementcashflow.append(inc)
        elif(cashflow[i+1]>cashflow[i]):
            inc=(cashflow[i+1]-cashflow[i])*100/cashflow[i]
            incrementcashflow.append(0)
    
    
avg_inc_cf=np.mean(incrementcashflow)     #average value of the increament of CFs 
stdev_inc_cf=np.std(incrementcashflow)    #Standard deviation of the increament of CF

#decimal rate of cf increament
if(cashflow[len(cashflow)-1]>0 and cashflow[0]>0):
    cagrcf=((cashflow[len(cashflow)-1]/cashflow[0])**(1/(len(cashflow)-1))-1)*100    
    cagrcf_binval=True
    
    if(avg_inc_cf<cagrcf):
        r=1+avg_inc_cf/(factor*100) 
        absolute_inc_rate_cf= 1+avg_inc_cf/100                  
    else:
        r=1+cagrcf/(factor*100)
        absolute_inc_rate_cf= 1+cagrcf/100                  

else:
    r=1+avg_inc_cf/(factor*100)
    absolute_inc_rate_cf= 1+avg_inc_cf/100                  

    
#print(incrementcf)

#calculation for the future Cash flow's in 2d array
future_cf_matrix=[]
if(r>0):
    for i in range(time):
        if(i<5): #assuming the rate same for first 5 years
            future_cf_array=[]     #determines future cf's w.r.t previous all years by proper rate
            for j in range(len(cashflow)):
                value=(cashflow[j])*(absolute_inc_rate_cf**(len(cashflow)-(1+j)))*(r**(i+1))
                future_cf_array.append(value)
            x=np.mean(future_cf_array)
            #x=cashflow[len(cashflow)-1]*r**(i+1)
            future_cf_matrix.append(future_cf_array)
            fut_cf.append(x)
            current_value_of_fut_cf=current_value_of_fut_cf+x/(1+inflation/100)**(1+i)
        elif(5<=i<10):  #rates taken to be half at next 5 yrs
            r1=(1+r)/2
            future_cf_array=[]
            for j in range(len(cashflow)):
                value=(future_cf_matrix[-1][j])*r1
                future_cf_array.append(value)
            x=np.mean(future_cf_array)
            #x=fut_cf[len(fut_cf)-1]*r1
            future_cf_matrix.append(future_cf_array)
            fut_cf.append(x)
            current_value_of_fut_cf=current_value_of_fut_cf+x/(1+inflation/100)**(1+i)

        elif(10<=i<15): # again half for next 5 years
            r2=(1+r1)/2
            future_cf_array=[]
            for j in range(len(cashflow)):
                value=(future_cf_matrix[-1][j])*r2
                future_cf_array.append(value)
            x=np.mean(future_cf_array)
            #x=fut_cf[len(fut_cf)-1]*r2
            future_cf_matrix.append(future_cf_array)
            fut_cf.append(x)
            current_value_of_fut_cf=current_value_of_fut_cf+x/(1+inflation/100)**(1+i)
        elif(15<=i<20):  #again half for next 5 yrs
            r3=(1+r2)/2
            future_cf_array=[]
            for j in range(len(cashflow)):
                value=(future_cf_matrix[-1][j])*r3
                future_cf_array.append(value)
            x=np.mean(future_cf_array)
            #x=fut_cf[len(fut_cf)-1]*r3
            future_cf_matrix.append(future_cf_array)
            fut_cf.append(x)
            current_value_of_fut_cf=current_value_of_fut_cf+x/(1+inflation/100)**(1+i)

        else:
            r4=(1+(1+r3)/2)/2   # final rate
            #r4=(1+r3)/2
            future_cf_array=[]
            for j in range(len(cashflow)):
                value=(future_cf_matrix[-1][j])*r1
                future_cf_array.append(value)
            x=np.mean(future_cf_array)
            #x=fut_cf[len(fut_cf)-1]*r4
            future_cf_matrix.append(future_cf_array)
            fut_cf.append(x)
            current_value_of_fut_cf=current_value_of_fut_cf+x/(1+inflation/100)**(1+i)
else:
    for i in range(time):
        future_cf_array=[]     #determines future cf's w.r.t previous all years by proper rate
        for j in range(len(cashflow)):
            value=(cashflow[j])*r**(len(cashflow)-(1+j)+(i+1))
            future_cf_array.append(value)
        x=np.mean(future_cf_array)
        #x=cashflow[len(cashflow)-1]*r**(i+1)
        future_cf_matrix.append(future_cf_array)
        fut_cf.append(x)
        current_value_of_fut_cf=current_value_of_fut_cf+x/(1+inflation/100)**(1+i)
                                                                   
all_fut_cf=np.sum(np.array(fut_cf))           #sum of all future CFs
int_val_cf=current_value_of_fut_cf*current_price/marketcap

#print(incrementcashflow)

print("CALCULATION USING DCF:")
print("")

print("Cash fllow growths: ",incrementcashflow)
print("Average increaase of cash flow till now: ",avg_inc_cf)
print("Future value of today's market cap by ",inflation,"% inflation: ",fut_mcp)
print("sum of all future cash flow: ",all_fut_cf)
print("Current intrinsic share price by DCF: ",int_val_cf)
print("Current share price with margin of safety: ",int_val_cf*(1-margin_of_safety/100))

years=np.arange(1,len(netprofit)+1)
years=years+starting_year-1

#######################################################
'''                  future prices                  '''
#######################################################

futureyears=np.arange(1,6)*5
futureyears=futureyears+current_year

futureprofits=[]
futureprice=[]
#print(futureyears)

for i in range(len(futureyears)):
    x=fut_np[5*(i+1)-1]
    futureprofits.append(x)
    y=x/(marketcap/current_price)*min([pe,medpe])
    futureprice.append(y)
    
#print(futureprofits)
futureprice=np.array(futureprice)

if(np.average(futureprice)<100):
    futureprice = [ '%.2f' % elem for elem in futureprice ]
elif(100<=np.average(futureprice)<10000):
    futureprice = [ '%.1f' % elem for elem in futureprice ]
else:
    futureprice = [ '%.0f' % elem for elem in futureprice ]

#######################################################
'''                   Plotting  Panel               '''
#######################################################


plt.figure(figsize = (37,20))
plt.plot(years,netprofit,'r-o',label="Net profit| avg: %1.2f" %avg_inc_np +"| std: %1.2f" %stdev_inc_np,linewidth=5,markersize=20)
plt.plot(years,cashflow,'g--d',label="Cash flow| avg: %1.2f" %avg_inc_cf +"| std: %1.2f" %stdev_inc_cf,linewidth=5,markersize=20)
plt.title("Company: %s" %company,size=75,fontname="cursive",fontweight="bold",color='green')
plt.xlabel("Years \n #Debt to Eq: %1.2f" %debt_to_equity +
           ";   ROCE: %1.2f" %roce +";   ROE: %1.2f" %roe +";  PE/avg(10y) PE: %1.2f" %pe +
           "/%1.2f"%medpe +"\n PB/avg PB: %1.2f"%pb +"/%1.2f"%medpb +";   PEG: %1.2f"%peg +
           ";   inflation: %1.1f" %inflation + "%"+";   Time: %d"%time +"Y;   Factor: %1.1f" %factor +
           "\n-----------------------------------------------------------------------------------------------\n" +
           r"$\bf{FUTURE\ STOCK\ PRICE:}$ (with PE: %1.2f" %min([pe,medpe])+")"+"\n %d" %futureyears[0] 
                                   + r":  $\bf{₹" + str(futureprice[0]) + ";}$"+
           "   %d" %futureyears[1] + r":  $\bf{₹" + str(futureprice[1]) + ";}$"+
           "   %d" %futureyears[2] + r":  $\bf{₹" + str(futureprice[2]) + ";}$"+
           "   %d" %futureyears[3] + r":  $\bf{₹" + str(futureprice[3]) + "}$"
           ,fontname="Times New Roman",fontweight="light",fontsize=60)

'''plt.figtext(0.1, -0.05, "\n" +r"$\bf{FUTURE\ STOCK\ PRICE:}$"+"\n %d" %futureyears[0] 
                        + r":  ₹$\bf{" + str(futureprice[0]) + "}$"+
";    %d" %futureyears[1] + r":  ₹$\bf{" + str(futureprice[1]) + "}$"+
";    %d" %futureyears[2] + r":  ₹$\bf{" + str(futureprice[2]) + "}$"+
";    %d" %futureyears[3] + r":  ₹$\bf{" + str(futureprice[3]) + "}$"
,fontname="Times New Roman",fontweight="light",fontsize=60)'''

plt.ylabel("Net profit/ Op Cash flow (cr)",fontname="Times New Roman",fontweight="light",fontsize=60)
plt.figtext(0.15,0.74,"Fut Growth: ["+str(R[0])+", "+str(R[1])+", "+str(R[2])+", "+str(R[3])+", "+str(R[4])+"]",fontsize=35,color='blue',fontweight='bold')
plt.figtext(0.17,0.7,"Intrinsic value:  (MOS: %d"%margin_of_safety+")", fontsize=50,backgroundcolor='yellow',fontname='cursive',fontweight='bold')
if(int_val_cf>0):
    plt.figtext(0.15,0.605,"By NP: ₹%1.2f" %int_val_np +" / %1.2f"%(int_val_np*(1-margin_of_safety/100))+"\nBy CF: ₹%1.2f" %int_val_cf + " / %1.2f" %(int_val_cf*(1-margin_of_safety/100)), fontsize=65,fontname="Times New Roman",fontweight="bold",color='blue',bbox = dict(facecolor = 'yellow', alpha = 0.5))
else:
    plt.figtext(0.15,0.655,"By NP: ₹%1.2f" %int_val_np +" / %1.2f"%(int_val_np*(1-margin_of_safety/100)), fontsize=65,fontname="Times New Roman",fontweight="bold",color='blue',bbox = dict(facecolor = 'yellow', alpha = 0.5))
#plt.figtext(0.15,0.6,"By CF: ₹%1.2f" %int_val_cf, fontsize=50,fontname="Times New Roman",fontweight="bold",color='blue',bbox = dict(facecolor = 'red', alpha = 0.5))
if(netprofit[len(netprofit)-1]>0 and netprofit[0]>0):
    plt.figtext(0.73,0.2,"CagrNP: %1.2f"%cagrnp +"%",fontsize=45,fontname="serif",backgroundcolor='yellow')
if(cashflow[len(cashflow)-1]>0 and cashflow[0]>0):
    plt.figtext(0.73,0.15,"CagrCF: %1.2f"%cagrcf +"%",fontsize=45,fontname="serif",backgroundcolor='yellow') 
#plt.figtext(0.035,-0.17,"By Sagar",fontname='cursive',fontsize=30,color='red',fontweight='bold',bbox = dict(facecolor = 'white', alpha = 0.5))
plt.legend()
plt.grid()
plt.xticks(fontsize=45,color='purple')
plt.yticks(fontsize=45,color='purple')
plt.legend(fontsize=45)
#plt.savefig('D:\\python files\\2d doppler new\\plots normalized\\file %d.jpg'%(file[i]))
plt.savefig('D:\\Financials\\Intrinsic value plots\\modified\\%s .jpg'%(company), bbox_inches='tight')
plt.show()


'''
##############################################################################
###################      Showing future NP and CF s      #####################
##############################################################################
print("")
print("")
print("###################################################################################")
print("###################################################################################")
print("###################################################################################")
print("###################################################################################")
print("")
print("")

print("Future Net Profit matrix:")
print(np.round_(future_np_matrix))

print("")
print("")
print("###################################################################################")
print("###################################################################################")
print("")
print("")
print("Future Cash Flow matrix:")
print(np.round_(future_cf_matrix))
'''