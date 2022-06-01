from importlib.resources import path
import turtle
import cv2
import math
import numpy as np
import pandas as pd
import os
import time
import matplotlib.pyplot as plt
import mss.tools, mss

#TO get image the open
from PIL import Image
  
# get image
filepath = r"CRINGE\unknown.png"


def carTrack():
    global t, img, dArea
    t = turtle.Turtle()
    dArea = turtle.Screen()
    turtle.bgpic(filepath)
    img = Image.open(filepath)
    # get width and height
    width, height = img.size
    # display width and height
    n_width, n_height = width + 81, height + 81
    dArea.setup(width=n_width, height=n_height)

    #Penup so theres no line (HOW TO GET RID OF THE ORGINAL TURTLE)
    t.penup()
    turtle.bgcolor('black')
    t.speed(10)
    t.lt(90)
    t.goto(-400, -200)


def fun(): #For tester function
    t.speed(1)
    t.fd(300)

def tester(): #Function to test the screenshoting of wherever our car is
    turtle.onkeypress(fun, "space")
    dArea.listen()

def neatGen(): #AI Algorithm
    pass

def pictureTaker(): #Takes pictures of car every 0.1 seconds
    time.sleep(10)
    with mss.mss() as sct:
        monitor0 = {"top": 160, "left": 160, "width": 500, "height": 500}   
        output0 = "sct-{top}x{left}_{width}x{height}.png".format(**monitor0)
        # Grab the data
        sct_img = sct.grab(monitor0)
        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output0)
        print(output0)

def rules(): #When car dies off
    img = cv2.imread(filepath) #this part just creates a mask over our current track just in case the greyscaling is an issue for rgb or hsv filtering
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    lower = np.array([0, 50, 50])
    upper = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    #cv2.imshow('image', img)
    #cv2.imshow('mask', mask)

def genData(): #Keeps track of each car of each Gens' time and distance in nodes
    global carCount
    carCount = 10

if __name__ == "__main__":
    carTrack()
    neatGen()
    rules()
    pictureTaker()
    genData()
    tester()
    turtle.exitonclick()


# while carCount > 0:
#     time.sleep(2)
#     r, g, b = img.getpixel((0, 0))
#     print("Red: {0}, Green: {1}, Blue: {2}".format(r, g, b))