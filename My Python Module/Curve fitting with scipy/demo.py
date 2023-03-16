import Lorentzianfitting as lft
import Gaussianfitting as gft
import Linefitting as lift
import numpy as np
import matplotlib.pyplot as plt


def main():
    
    #Lorentzisn demo fit
    x=np.linspace(0,20,201)      #data along x axis
    y=50/(5+(x-5)**2)             #data along y axis
    random_noise=np.random.uniform(low=-0.4,high=0.4,size=(len(y)))
    y=y+random_noise
    
    fit_y,parameters,string=lft.Lorentzfit(x,y)
    plt.plot(x,y,'ko')
    plt.plot(x,fit_y)
    print(string)
    plt.title("Lorentzian fit of data \n"+string,fontname="Times New Roman")
    plt.grid()
    plt.show()
    
    print(*parameters)
    print('FWHM= ', parameters[1])
    
    # Gaussian fit demo
    x=np.linspace(0,20,201)      #data along x axis
    y=10*np.exp(-(x-5)**2/5)             #data along y axis
    random_noise=np.random.uniform(low=-0.4,high=0.4,size=(len(y)))
    y=y+random_noise
        
    fit_y,parameters,string=gft.Gaussfit(x,y)

    plt.plot(x,y,'ko')
    plt.plot(x,fit_y)
    plt.title("Gaussian fit of data \n"+string,fontname="Times New Roman")
    plt.grid()
    plt.show()
    
    print(*parameters)
    print('FWHM= ', 2.355*parameters[0])
    
    
    
    #demo fit for linefit
    x=np.linspace(0,20,201)
    y=2*x+5
    random_noise=np.random.uniform(low=-1,high=1,size=(len(y)))
    y=y+random_noise
    
    line,parameters,string=lift.linefit(x,y)
    plt.plot(x,y,'ko')
    plt.title("Linear fit of data \n"+string,fontname="Times New Roman")
    plt.grid()
    plt.plot(x,line)
    plt.show()
    

if __name__=='__main__':
    main()