# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:01:13 2023

@author: sagar
"""

import numpy as np
import matplotlib.pyplot as plt
import concurrent.futures
import matplotlib
import time


matplotlib.rcParams['figure.dpi'] = 500  # highres display

t_start=time.time()
def create_random_root(n):
    root=[]
    Re=np.random.uniform(low=-1,high=1,size=n)
    Im=np.random.uniform(low=-1,high=1,size=n)
    for i in range(n):
        root.append(Re[i]+Im[i]*1j)
    return(root)



root = [0.5+0.35j, -0.9+0.35j,-0.45-0.4125j,-0.4+0.9j,0.65-0.48j]
#root = [0.5*np.exp(1j * i * 2 * np.pi / 4) for i in range(4)]
#root=create_random_root(6)

iteration = 50
root=np.array(root)
colors = np.linspace(0, 1, len(root))

print("Roots:")
for i in range(len(root)):
    print(f"z{i+1}:    {root[i]: .3f}")

def f(z):
    val=1
    for i in range(len(root)):
        val = val*(z-root[i])
    return(val)

def df(z):
    val = 0
    for i in range(len(root)):
        mult=1
        for j in range(len(root)):
            if(j!=i):
                mult = mult*(z-root[j])
        val += mult
    return(val)

def iteration_step(z):
    return z - f(z) / df(z)

def colour_the_complex_plane(z, root, colors):
    dist = np.abs(z[:, :, np.newaxis] - root)
    try:
        nearest = np.argmin(dist, axis=2)
    except:
        nearest = 0
    output = colors[nearest]
    return output

res=150

x = np.linspace(-max(abs(root.real))*1.1,max(abs(root.real))*1.1,int(2*res*(max(abs(root.real))+1)))
y = np.linspace(-max(abs(root.imag))*1.1,max(abs(root.imag))*1.1,int(2*res*(max(abs(root.imag))+1)))

X, Y = np.meshgrid(x, y)
z = X + Y * 1j

# Define a function for parallelizing the iterations
def parallel_iterations(iteration_step, z, num_iterations):
    for i in range(num_iterations):
        z = iteration_step(z)
    return z

# Number of parallel threads (adjust as needed)
num_threads = 8

# Split the total iterations into chunks for parallel execution
iterations_per_thread = iteration // num_threads
iterations_list = [iterations_per_thread] * num_threads

# If the total iterations is not divisible evenly by num_threads, distribute the remaining iterations
iterations_list[-1] += iteration % num_threads

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(parallel_iterations, iteration_step, z.copy(), iterations) for iterations in iterations_list]
    concurrent.futures.wait(futures)

# Combine the results from parallel iterations
for future in futures:
    z = future.result()

output = colour_the_complex_plane(z, root, colors)
X=output.shape[0]
Y=output.shape[1]


output=np.flip(output,axis=0)

plt.imshow(output,cmap='jet',extent=[min(x),max(x),min(y),max(y)])
for i in range(len(root)):
    if(abs(root[i].real)<=max(x) and abs(root[i].imag)<=max(y) ):
        plt.scatter(root[i].real,root[i].imag, color='red', marker='o')
        plt.text(root[i].real,root[i].imag, r'z$_{%d}$'%(1+i), color="white", fontsize=10, ha='left', va='bottom')
plt.title(r"NEWTON'S FRACTAL $\ \ by\ \$\alpha\widetilde g\alpha R$")
plt.grid(color="blue",linewidth=0.5)
plt.xlabel("Re(z)",fontsize=7)
plt.ylabel("Im(z)",fontsize=7)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.show()

print("\n\nTime taken:   ",time.time()-t_start)