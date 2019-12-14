"""CSCI-603: Lab 2
    Author: Michael Abdelshahid

    This is a demo of the Forest at Night"""
import turtle as turtle
import random
import math

math.sqrt(2)
wood = (100)
halfwood = ((wood / 2) * math.sqrt(2))
math.cos(math.radians(45))
amtwood = (200) + (2*(100 * math.cos((45))))
halfamtwood = ((amtwood / 2)* math.sqrt(2))

# global constants for window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

def init():
    """Initialize for drawing. (-200,-400) is in the lower left and
    (800, 800) is in the upper right.
    :pre: pos (800, 400), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH, WINDOW_WIDTH*2, WINDOW_HEIGHT)
    turtle.speed(0)

def trunk(x):
    turtle.left(90)
    turtle.forward(x)

def pine_tree():
    """ Makes pine tree with random size trunk height"""
    x = random.randint(50,200)
    trunk(x)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(100)
    return x + 40

def maple_tree():
    """ Makes maple tree with random size trunk and height """
    x = random.randint(50,150)
    trunk(x)
    turtle.right(90)
    turtle.circle(25)
    turtle.right(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(100)
    return x + 40

def nighthouse():
    """ Makes night house with calculated wood used """
    turtle.left(90)
    turtle.forward(wood)
    turtle.right(45)
    turtle.forward(halfwood)
    turtle.right(90)
    turtle.forward(halfwood)
    turtle.right(45)
    turtle.forward(wood)
    turtle.right(90)
    turtle.forward(100)

def bush_tree():
    """ Makes bush tree with random size trunk and height """
    x = random.randint(50,100)
    trunk(x)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(100)
    return x + 40

def star(wood, halfwood):
    """ Makes star 10 pixels above the height of trees and house """
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(wood + halfwood + 10)
    turtle.pendown()
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(25)
    turtle.left(45)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(25)
    turtle.left(45)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(25)
    turtle.left(45)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(50)
    turtle.hideturtle()

def dayhouse():
    """ Makes day house with calculated amount of woods used """
    turtle.penup()
    turtle.setpos(60,30)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(amtwood)
    turtle.right(45)
    turtle.forward(halfamtwood)
    turtle.right(90)
    turtle.forward(halfamtwood)
    turtle.right(45)
    turtle.forward(amtwood)
    turtle.right(90)
    turtle.forward(amtwood)
    turtle.right(180)
    turtle.forward(amtwood)
    return amtwood

def sun(amtwood, halfamtwood):
    """ Makes sun 10 pixels above the height of the house """
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(amtwood + halfamtwood + 10)
    turtle.pendown()
    turtle.circle(50)

def main():
    """
    The main function.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    trees = int(input("How many trees in your forest? "))
    while trees != 1 and trees != 2 and trees != 3 and trees != 4:
        trees = int(input("How many trees in your forest? "))
    house = (input("Is there a house in the forest (yes/no)? "))
    while house != 'yes' and house != 'no':
        house = input("Is there a house in the forest (yes/no)? ")

    init()
    for x in range(0,trees):
        y = random.randint(0,2)
        if y == 0:
            y = pine_tree()
        if y == 1:
            y = maple_tree()
        if y == 2:
            y = bush_tree()
    if house == 'yes' or 'no':
        if house == 'yes':
            nighthouse()
    star(wood, halfwood)
    input("Night is done. Press enter for day")
    turtle.clear()

    turtle.setworldcoordinates(-WINDOW_WIDTH, -WINDOW_WIDTH, WINDOW_WIDTH*2, WINDOW_HEIGHT*2)
    """Initialize for drawing. (-400,-400) is in the lower left and
    (800, 800) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None"""

    dayhouse()
    amount_woods = ((4 * 200) + (2 * (100 * math.cos((45)))))
    print('We have',amount_woods,'units of lumber for building')
    sun(amtwood, halfamtwood)
    input("Day is done. Press enter to quit")
    turtle.bye()

    # turtle.mainloop()

if __name__ == "__main__":

    main()
