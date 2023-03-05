# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:35:06 2022

@author: mrsag
"""

#######################################################
import turtle
import time
import random
#######################################################


speed=10
spacedelay=20
size=600
score=0
t=0.05*20/speed

extrasize=100
#setup the screen

wn=turtle.Screen()
wn.title("Snake game")
wn.bgcolor("green")
wn.setup(width=size+extrasize,height=size+extrasize)
wn.tracer(0)

# Boundary of the snake
p1=(size/2+20,size/2+20)
p2=(size/2+20,-size/2-20)
p3=(-size/2-20,-size/2-20)
p4=(-size/2-20,size/2+20)

turtle.penup()
turtle.goto(p1)
turtle.pendown()
turtle.pencolor("magenta")
turtle.width(4)
turtle.goto(p2)
turtle.goto(p3)
turtle.goto(p4)
turtle.goto(p1)
turtle.hideturtle()

turtle.penup()
#######################################################

#snake head

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction="stop"
head.turtlesize(0.8)


#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)
food.turtlesize(0.8)


#snake body
segment=[]

#scoring
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,(size+extrasize/5)/2+7)
pen.write("Score: 0",align="center",font=("Courier",24))

#function
def go_up():
    if(len(segment)>0):
        if(head.direction !="down"):
            head.direction="up"
    elif(len(segment)==0):
        head.direction="up"
def go_down():
    if(len(segment)>0):
        if(head.direction !="up"):
            head.direction="down"
    elif(len(segment)==0):
        head.direction="down"
def go_left():
    if(len(segment)>0):
        if(head.direction !="right"):
            head.direction="left"
    elif(len(segment)==0):
        head.direction="left"
def go_right():
    if(len(segment)>0):
        if(head.direction !="left"):
            head.direction="right"
    elif(len(segment)==0):
        head.direction="right"

#Keyboard instruction
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")


def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+spacedelay)
    elif head.direction=="down":
        y=head.ycor()
        head.sety(y-spacedelay)
    elif head.direction=="left":
        x=head.xcor()
        head.setx(x-spacedelay)
    elif head.direction=="right":
        x=head.xcor()
        head.setx(x+spacedelay)

#main loop

while True:
    wn.update()
    
    #check for a collision with the screen border
    if(size<2*abs(head.xcor()) or size<2*abs(head.ycor())):
       time.sleep(0.5)
       head.goto(0,0)
       head.direction="stop"
       
       for parts in segment:
           parts.goto(2*size,2*size)
           
       segment.clear()
       score=0
    
    #check for a collision with the head and food
    if head.distance(food)<20:
    #if (np.sqrt((head.xcor()-food.xcor())**2+(head.ycor()-food.ycor())**2)<20):
        #move the food to a random position
        x=random.randint(-size/2+20,size/2-20)
        y=random.randint(-size/2+20,size/2-20)
        food.goto(x,y)
        
        #add snake body
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.turtlesize(0.8)
        new_segment.penup()
        segment.append(new_segment)
        
        # Scoring
        score = score+10
        pen.clear()
        pen.write("Score: {}".format(score),align="center",font=("Courier",24))
    # adding the body
    for i in range(len(segment)-1,0,-1):
        x=segment[i-1].xcor()
        y=segment[i-1].ycor() 
        segment[i].goto(x,y)
        
    #move the first body part
    if len(segment)>0:
        x=head.xcor()
        y=head.ycor()
        segment[0].goto(x,y)
        
    move()
    
    # check for body collision
    for part in segment:
        if part.distance(head)<20*0.8:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction="stop"
            
            for parts in segment:
                parts.goto(2*size,2*size)
                
            segment.clear()
            score=0
            
    time.sleep(t)
    
    
wn.mainloop()
