#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: October 24, 2019

import turtle
def doAction(t,c):
    if c == 'F':
        t.forward(50)
    elif c == 'B':
        t.backward(50)
    elif c == 'L':
        t.left(90)
    elif c == 'R':
        t.right(90)
    elif c == 'S':
        t.stamp()
    elif c == '^':
        t.up()
    elif c == 'v':
        t.down()
    elif c == 'l':
        t.left(45)
    elif c == 'r':
        t.right(45)
    elif c == 'p':
        t.pencolor("purple")
    else:
        print("Error: do not know the command:",c)
  
def main():
    silas = turtle.Turtle()
    myWin = turtle.Turtle()
    commands = input("Please enter a command string: ")
    for ch in commands:
        doAction(silas,ch)
    print("See graphics window for your image")
    myWin.exitonclick()
  
main()