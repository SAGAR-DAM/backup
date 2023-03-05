from vpython import *
import numpy as np

floor=box(pos=vector(0,0,0),length=4,height=0.2,width=4,color=color.red) #defining a box at specific position and dimension
ball=sphere(pos=vector(0,5,0),radius=1,color=color.green)  #defining a sphere at specific position and dimension
ball1=sphere(pos=vector(0,-5,0),radius=1,color=color.yellow)

ball.velocity=vector(0,10,0)
ball1.velocity=vector(0,-10,0)

dt=0.01

while True:
    rate(200)
    ball.pos=ball.pos+ball.velocity*dt
    if ball.pos.y<ball.radius:
        ball.velocity.y=-(ball.velocity.y)
    else:
        ball.velocity.y=ball.velocity.y-9.8*dt
        
    ball1.pos=ball1.pos+ball1.velocity*dt
    if abs(ball1.pos.y)<ball1.radius:
        ball1.velocity.y=-(ball1.velocity.y)
    else:
        ball1.velocity.y=ball1.velocity.y+9.8*dt
