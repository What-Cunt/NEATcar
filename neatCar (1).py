import turtle
from tkinter import Image
import cv2
import math
import numpy as np
import pandas as pd
import os
import time
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageGrab
import mss
import mss.tools
import pyautogui
import hashlib
import timeit
#Don't need to pip install timeit and hashlib packages. They're already preinstalled as of python 2.5=>

def carTrack(): # Sets up Car Track
   global filepath, t, img, dArea, gen, num
   filepath = os.environ.get("FILEPATH") #Set in your path the name as FILEPATH and the value as the directory to the carPictures folder
   print(filepath)
   t = turtle.Turtle()
   dArea = turtle.Screen()
   turtle.bgpic(filepath + r"\carTrack.png")
   img = Image.open(filepath + r"\carTrack.png")
   gen = 1
   num = 1
   # get width and height
   width, height = img.size
   # display width and height
   n_width, n_height = width + 81, height + 81
   dArea.setup(width=n_width, height=n_height)
   t.penup()
   turtle.bgcolor('black')
   t.pencolor('green')
   t.speed(10)
   t.lt(90)
   t.goto(-400, -200)

def fwrd(): #For tester function
   t.fd(5)
def bck():
   t.bk(5)
def rght():
   t.rt(90)
def lft():
   t.lt(90)

def main(): #Function to test the screenshoting of wherever our car is
   global carCoords, timedDeath, gen, timedDeath, carTimes, bestTimes, num
   startTime = time.time()
   highest = 0
   for i in range(100):
       # Move the car
       turtle.onkeypress(fwrd, "Up")
       turtle.onkeypress(bck, "Down")
       turtle.onkeypress(lft, "Left")
       turtle.onkeypress(rght, "Right")
       dArea.listen()
       dArea.update()
       #Picture taking
       # Takes pictures of car every 0.1 seconds (100 miliseconds is not fast. May ned to use PIL to optimize? Transfer away from pygame to optimize further)
       carCoords = pyautogui.locateOnScreen(filepath + r"\upcar.png", confidence=0.95) #5% alpha- pval < null = surprising. At 100% CL, pixels may change before cars hit it and car will die wrongly
       if carCoords == None:
           carCoords = pyautogui.locateOnScreen(filepath + r"\leftcar.png", confidence=0.95)
           time.sleep(0.1)
           if carCoords == None:
               carCoords = pyautogui.locateOnScreen(filepath + r"\rightcar.png", confidence=0.95)
               time.sleep(0.1)
               if carCoords == None:
                   carCoords = pyautogui.locateOnScreen(filepath + r"\downcar.png", confidence=0.95)
                   time.sleep(0.1)
                   if carCoords == None: #Kills car and resets it to original position
                       endTime = time.time()
                       timedDeath = round(endTime - startTime, 3)
                       #print("Elapsed time is {}".format(timedDeath))
                       carTimes[gen] = timedDeath
                       print(carTimes)
                       gen += 1
                       t.goto(-400, -200)
                       t.setheading(90)
                       if len(carTimes) == 5: #Update gen
                           for x in carTimes:
                               if carTimes[x] > highest:
                                   highest = carTimes[x]
                               else:
                                   continue
                           bestTimes[num] = highest
                           carTimes.clear()
                           num += 1
                           gen = 1
                           print(bestTimes)
                       break
       im1 = pyautogui.screenshot()
       im2 = pyautogui.screenshot('theCar.png', region=carCoords)  # left, top, width, height
       time.sleep(0.1)
       #print(carCoords)

def neatGen(): #AI Algorithm
   pass

'''
def complexityTracker(): #Should check the amount of time each process takes. Temporary function to optimize time or even space complexity.
    print(timeit.timeit(complexityTracker, number=100))
    return hashlib.sha256(b'Code profiling').hexdigest()
''' #Work in progress. https://stackify.com/how-to-optimize-python-code/


def genData(): #Keeps track of each car of each Gens' time and distance in nodes
   global carTimes, bestTimes
   carCount = 10
   bestTimes = dict() #Best car times from each gen
   carTimes = dict() #Current car times
   #Next part is solely for graphing plots over time


if __name__ == "__main__":
   carTrack()
   neatGen()
   #masking()
   genData()
   #complexityTracker()
   while True:
       main()



""""
def masking(): #When car dies off
   img = cv2.imread(filepath) #this part just creates a mask over our current track just in case the greyscaling is an issue for rgb or hsv filtering
   hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   lower = np.array([0, 50, 50])
   upper = np.array([130, 255, 255])
   mask = cv2.inRange(hsv, lower, upper) #Black and white track scaling
   #cv2.imshow('image', img)
   cv2.imshow('mask', mask)
"""