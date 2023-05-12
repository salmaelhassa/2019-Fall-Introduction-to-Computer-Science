#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: Novemeber 11, 2019

import turtle

def setup(t, dist, col):
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)

def triangle(t,length):
    if length>10:
        for _ in range(3):
            t.forward(length)
            t.left(120)
        triangle(t,length/2)


def nestedTriangle(t,length):
    if length>10:
        for _ in range(3):
            t.forward(length)
            t.left(120)
            nestedTriangle(t,length/2)

def main():
    n = int(input('Enter length: '))
    tom = turtle.Turtle()
    setup(tom, -100, "darkgreen")
    triangle(tom, n)
    tess = turtle.Turtle()
    setup(tess, 100, "steelblue")
    nestedTriangle(tess, n)

if __name__ == "__main__":

    main()