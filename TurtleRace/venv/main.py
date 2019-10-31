from turtle import *
from random import seed
from random import random
from random import randint


def drawbox(posx,posy,bwidth,bheight):
    boxturt = Turtle()
    boxturt.penup()
    boxturt.goto(posx,posy)
    boxturt.pendown()
    boxturt.forward(bwidth)
    boxturt.rt(-90)
    boxturt.forward(bheight)
    boxturt.rt(-90)
    boxturt.forward(bwidth)
    boxturt.rt(-90)
    boxturt.forward(bheight)

def drawgrid(posx,posy,datarange,scale):
    boxturt = Turtle()
    boxturt.penup()
    boxturt.goto(posx,posy)
    boxturt.pendown()
    unitlen = 1*scale
    for step in range(datarange):
        boxturt.forward(unitlen)

        if step%10==datarange%10:
            boxturt.write(step)

def randtup():
    tup1 = randint(0,1)
    tup2 = randint(0,1)
    tup3 = randint(0,1)

    return tup1,tup2,tup3

def drawdownline(pos):
    aaa = Turtle()
    aaa.penup()
    aaa.setpos(pos)
    aaa.pendown()
    aaa.lt(-90)
    aaa.fd(100)

def hidenTurt(xturt,datax,datay,step,scale):
    secturt = xturt
    secturt.fd(datay[step]*scale)
    secturt.lt(90)
    secturt.pensize(5)
    secturt.pencolor(randtup())
    secturt.pendown()
    secturt.forward(datax[step]*scale)
    secturt.penup()
    secturt.setpos(-300,-300)
    secturt.setheading(0)


def Graph(posx, posy,datax,datay,scale):
    graphturt = Turtle()
    graphturt.penup()
    graphturt.setpos(posx,posy)

    for step in range(len(datax)):

        hidenTurt(graphturt,datax,datay,step,scale)

def popArray(length):
    data1 = []
    for step in range(length):
        data1.append(randint(0,100))
    return data1

seed()

datarange = 100;

dataset1 = popArray(10)
dataset2 = popArray(10)
dataset1.sort()
dataset2.sort()

colordata = []

scale = 5

graphposx = -300
graphposy = -300
for i in range(len(dataset1)):
    print(dataset1[i],", ",dataset2[i])

drawgrid(graphposx,graphposy,datarange,scale)
Graph(graphposx,graphposy,dataset1,dataset2,scale)


#
#main = Turtle()
#main.penup()
#main.goto(-100,50)
#
#for step in range(10):
#    main.write(step)
#   pos = main.position()
#    drawdownline(pos)
#    main.forward(20)



exitonclick()
