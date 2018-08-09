"""
File:  raindrops.py
Author: Eugene Chang
"""

import turtle as t
import math
from random import*

def MAX_RAINDROPS():
    return 100

def MAX_RADIUS():
    return 20

def MAX_RIPPLES():
    return 7

def MIN_RIPPLES():
    return 3

def SCREEN_WIDTH():
    return 600

def SCREEN_HEIGHT():
    return 750

def init():
    """Initializes turtle window by drawing border boundary and positioning the turtle in the center.
    """
    t.setup(SCREEN_WIDTH(), SCREEN_HEIGHT(), 300, 25)
    t.title("RainDrops!")
    t.bgcolor("black")
    t.pencolor("white")
    t.speed(99999)
    t.home()

def drawRainDrops(n):
    """
    generates raindrops in random locations within the boundary.
    """
    if n == 0:
        return
    else:
        t.up()
        raindropLocation()
        drawRainDrops(n-1)



def raindropLocation():
    """
    determines the location of each raindrop, and makes sure it lands
    within the boundary.

    """
    maxDiam = 2 * MAX_RADIUS()
    randX = randint(-math.ceil((SCREEN_WIDTH() / 2)) + maxDiam, math.floor((SCREEN_WIDTH() / 2)) - maxDiam)
    randY = randint(-math.ceil((SCREEN_HEIGHT() / 2)) + maxDiam, math.floor((SCREEN_HEIGHT() / 2)) - maxDiam)
    radius = randint(1, MAX_RADIUS())
    numRipples = randint(MIN_RIPPLES(), MAX_RIPPLES())

    t.up()
    t.goto(randX, randY)
    drawSingleDrop(numRipples, radius)

def drawSingleDrop(num, rad):
    """
    draws the raindrop with a random fill color and with a random number of ripples
    """
    move = rad
    sum = 0
    firstCircle = 0
    while num > 0:
        t.up()
        t.fd(move)
        t.lt(90)
        t.down()

        r = random()
        g = random()
        b = random()

        if firstCircle == 0:
            t.fillcolor(r,g,b)
            t.begin_fill()
            t.circle(rad)
            t.end_fill()
            firstCircle = 1

        t.circle(rad)
        t.rt(90)
        sum = sum + (math.pi * rad * rad)
        rad = rad + move
        num -= 1

def main():
    """
    main function which prompts user for input of # of raindrops,
    initializes turtle, checks number of raindrops, running program.
    """
    n = int(input("Raindrops (1-100): "))
    if n > 100 or n <= 0:
        print("Raindrops must be between 1 and 100 inclusive.")
    else:
        init()
        drawRainDrops(n)
        t.done()


main()