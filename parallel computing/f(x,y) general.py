import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
import time
import multiprocessing

import matplotlib as mpl

mpl.rcParams['figure.dpi']=500 # highres display
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12
mpl.rcParams['font.weight'] = 'bold'
# mpl.rcParams['font.style'] = 'italic'

t_start=time.time()


# Define your range and resolution
x_range = (-1, 3)
y_range = (-1, 3)
x_resolution = 3001
y_resolution = 3001

# Create the grid
x = np.linspace(*x_range, x_resolution)
y = np.linspace(*y_range, y_resolution)
X, Y = np.meshgrid(x, y)


# Define the function
# def f(x,y):
#     if(x<=1):
#         if(-0.2<=x<=0.2):
#             if(y<=-0.7):
#                 return(0.999)
#             elif(-0.7<y<0.2):
#                 return(0.999*np.exp(-5*(y+0.7)))
#             else:
#                 return(0)
#         else:
#             if(y<=-0.7):
#                 return(0.999)
#             elif(-0.7<y<0.2):
#                 return(0.999*np.exp(-5*(y+0.7))*np.exp(-5*(abs(x)-0.2 )))
#             else:
#                 return(0)
#     elif(x>1):
#         return(f(x-2,y))

def f(x,y):
    return(x**2+y**2)

f = np.vectorize(f, otypes=[np.float])

# Define the function to be parallelized
def parallel_func(args):
    x_start, x_end, y_start, y_end = args
    Z = f(X[y_start:y_end, x_start:x_end], Y[y_start:y_end, x_start:x_end])
    return Z

if __name__ == '__main__':
    # Get the number of cores
    num_cores = multiprocessing.cpu_count()

    # Define the ranges for each core
    ranges = []
    for i in range(num_cores):
        x_start = i * x_resolution // num_cores
        x_end = (i + 1) * x_resolution // num_cores if i < num_cores - 1 else x_resolution
        ranges.append((x_start, x_end, 0, y_resolution))

    # Create a pool of workers
    with Pool(num_cores) as p:
        results = p.map(parallel_func, ranges)

    # Combine the results
    Z = np.concatenate(results, axis=1)

    # Plot the result
    plt.imshow(Z, cmap="hot", extent=[*x_range, *y_range])
    plt.colorbar()
    plt.show()
    
    
    print(f"{time.time()-t_start}")
