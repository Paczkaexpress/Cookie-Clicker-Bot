# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:50:51 2019

@author: Erazer
"""

import pyautogui
import time
import sys
import numpy as np
import cv2
from pynput import keyboard
import _thread
from PIL import Image
from PIL import ImageGrab


fSystemWait = False
#gCookiePos =


def clickCookie():
     while(1):
          if fSystemWait == False:
               pyautogui.click(120, 410, 4)
               pyautogui.click(180, 445, 4)
               pyautogui.click(180, 410, 4)
               pyautogui.click(120, 445, 4)
#               time.sleep(0.001)

def onPress(key):
     global fSystemWait
     try:
          if key.char == 'q':
               sys.exit()
#               wait for start command
          if key.char == 'w':
               fSystemWait = True
          if key.char == 's':
               fSystemWait = False
     except AttributeError:
          pass

def clickUpdate():
     step = 60
     nrOfUpdates = 9
     while(1):
          if fSystemWait == False:
               for i in range(nrOfUpdates):
                    pyautogui.click(700, 850 - i*step, 1)
               time.sleep(30)

def clickUpgrade():
     while(1):
          if fSystemWait == False:
               pyautogui.click(650, 250 , 1)
               time.sleep(1)

def getPrintscreen():
    while(1):
        img = ImageGrab.grab()
        imgPath = 'pictures\\'
        img.save(imgPath + 'printscreen.jpg')
        print("print screen saved")
        rawImg = cv2.imread(imgPath + 'printscreen.jpg')
        print("print screen loaded")
        imgGrey = cv2.cvtColor(rawImg, cv2.COLOR_BGR2GRAY)
        print("print screen converted to grey scale")
#        imgGrey = cv2.GaussianBlur(imgGrey, (3, 3), 0)
#        print("print screen blurred")
#        sift = cv2.SIFT()
        sift = cv2.xfeatures2s.SIFT_create()
        kp = sift.detect(imgGrey, None)
        imgSift = cv2. drawKeypoins(imgGrey, kp)
        cv2.write(imgPath + 'siftKeypoints.jpg', imgSift)

        # detect edges in the image
        imgEdged = cv2.Canny(imgGrey, 180, 200)
        print("Image edges detected")

        # image close operation

        Imgkernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
        Imgclosed = cv2.morphologyEx(imgEdged, cv2.MORPH_CLOSE, Imgkernel)
        print("Image close operation")

        circles = cv2.HoughCircles(imgEdged,cv2.HOUGH_GRADIENT,1,10,
                            param1=90,param2=90,minRadius=0,maxRadius=150)
#
        circles = np.uint16(np.around(circles))
        print("Hough transformation performed")
#
        for i in circles[0,:]:
            print(i)
            # draw the outer circle
            cv2.circle(rawImg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(rawImg,(i[0],i[1]),2,(0,0,255),3)




        print("save modified jpg")
        cv2.imwrite(imgPath + 'rawImg.jpg', rawImg)
        cv2.imwrite(imgPath + 'imgEdged.jpg', Imgclosed)
#        cv2.imshow("Edged", edged)
#        cv2.waitKey(0)
        time.sleep(300)

def featureExtraction():
    a = 10 #random comment

if __name__ == "__main__":
#     start thread
#     _thread.start_new_thread(clickCookie, ())
#     _thread.start_new_thread(clickUpdate, ())
#     _thread.start_new_thread(clickUpgrade, ())
     _thread.start_new_thread(getPrintscreen, ())

     with keyboard.Listener(on_press=onPress) as listenter:
          listenter.join()
