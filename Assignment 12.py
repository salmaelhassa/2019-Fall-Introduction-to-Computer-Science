#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: September 20, 2019
#This program demonstrates the shades of blue

import turtle				

turtle.colormode(255)		
tess = turtle.Turtle()		
tess.shape("turtle")		
tess.backward(100)			 

#For 0,10,20,...,250
for i in range(0,255,10):
     tess.forward(10)		
     tess.pensize(i)		
     tess.color(0,0,i)		
