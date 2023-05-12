#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: October 03, 2019
#This program prompts the user for 5 whole integers.

import turtle

wn = turtle.Screen()

tur = turtle.Turtle()

for i in range(5):
	angle = int(input('Enter a number: '))
	tur.left(angle)
	tur.forward(100)

wn.exitonclick()
