import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
import time

import matplotlib as mpl

mpl.rcParams['figure.dpi']=500 # highres display
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12
mpl.rcParams['font.weight'] = 'bold'
# mpl.rcParams['font.style'] = 'italic'

t_start=time.time()


# Define the function
def f(x,y):
    if(x<=1):
        if(-0.2<=x<=0.2):
            if(y<=-0.7):
                return(0.999)
            elif(-0.7<y<0.2):
                return(0.999*np.exp(-5*(y+0.7)))
            else:
                return(0)
        else:
            if(y<=-0.7):
                return(0.999)
            elif(-0.7<y<0.2):
                return(0.999*np.exp(-5*(y+0.7))*np.exp(-5*(abs(x)-0.2 )))
            else:
                return(0)
    elif(x>1):
        return(f(x-2,y))
f = np.vectorize(f, otypes=[np.float])


# Create the grid
x, y = np.linspace(-1, 1, 2001), np.linspace(-1, 1, 2001)
X, Y = np.meshgrid(x, y)

def parallel_func(args):
    x_start, x_end, y_start, y_end = args
    Z = np.zeros((y_end-y_start, x_end-x_start))
    
    Z = f(X[y_start:y_end, x_start:x_end], Y[y_start:y_end, x_start:x_end])
    return Z

# Define the ranges for each quadrant
ranges = [(0, 500, 0, 500), (0, 500, 500, 1000), (500, 1000, 0, 500), (500, 1000, 500, 1000)]

if __name__ == '__main__':
    # Create a pool of workers
    with Pool(4) as p:
        results = p.map(parallel_func, ranges)

    # Combine the results
    Z = np.block([[results[0], results[2]], [results[1], results[3]]])

    # Plot the result
    plt.imshow(Z, cmap="hot", extent=[-1, 1, -1, 1])
    plt.colorbar()
    plt.show()


    print(f"{time.time()-t_start}")