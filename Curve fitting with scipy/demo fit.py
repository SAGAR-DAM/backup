import Lorentzianfitting as lft
import Gaussianfitting as gft
import Linefitting as lift
import numpy as np
import matplotlib.pyplot as plt


def main():

    #Lorentzisn demo fit
    x=np.linspace(0,20,201)      #data along x axis
    y=50/(5+(x-5)**2)             #data along y axis
    random_noise=np.random.uniform(low=-1,high=1,size=(len(y)))
    y=y+random_noise
    
    fit_y,parameters=lft.Lorentzfit(x,y)
    plt.plot(x,y,'ko')
    plt.plot(x,fit_y)
    plt.show()
    
    print(*parameters)
    print('FWHM= ', 2.355*parameters[0])
    
    # Gaussian fit demo
    x=np.linspace(0,20,201)      #data along x axis
    y=10*np.exp(-(x-5)**2/5)             #data along y axis
    random_noise=np.random.uniform(low=-1,high=1,size=(len(y)))
    y=y+random_noise
        
    fit_y,parameters=gft.Gaussfit(x,y)
    plt.plot(x,y,'ko')
    plt.plot(x,fit_y)
    plt.show()
    
    print(*parameters)
    print('FWHM= ', 2.355*parameters[0])
    
    
    
    #demo fit for linefit
    y=2*x+5
    random_noise=np.random.uniform(low=-1,high=1,size=(len(y)))
    y=y+random_noise
    
    line,parameters=lift.linefit(x,y)
    plt.plot(x,y,'ko')
    plt.plot(x,line)
    plt.show()
    
if __name__=='__main__':
    main()
