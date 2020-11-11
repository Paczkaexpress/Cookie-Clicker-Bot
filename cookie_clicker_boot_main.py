"""
Created on Wed Feb 20 21:50:51 2019

@author: 
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

def clickCookie():
     """
          @brief: Finds and click the cookie
          @description: The target of that function is to find every clickable cookie
          Including the golden ones. 

          The system needs to recalibrate the position of the main cookie time to time 
     """
     counter = 0
     while(1):
          if fSystemWait == False:
               if counter % 2000 == 0:
                    picturePos = pyautogui.locateOnScreen('pictures/bigCookie.png', grayscale=True, confidence = 0.6)
               if counter % 10 == 0:
                    goldenCookiePos = pyautogui.locateOnScreen('pictures/goldenCookie.png', grayscale=True, confidence = 0.4)
                    if goldenCookiePos != None:
                         print(f"Found the golden one at {goldenCookiePos}")
                         pyautogui.click(goldenCookiePos)
               counter += 1
               if picturePos != None:
                    pyautogui.tripleClick(picturePos)

          pyautogui
def onPress(key):
     global fSystemWait
     try:
          if key.char == 'q':
               sys.exit()
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
               buildingPos = pyautogui.locateOnScreen('pictures/cursorPos.png', confidence = 0.8)
               if buildingPos != None:
                    for i in range(nrOfUpdates,0,-1):
                         pyautogui.click(buildingPos.left+50, buildingPos.top + i*step, 1)
               time.sleep(30)

def clickUpgrade():
     while(1):
          if fSystemWait == False:
               upgradePos = pyautogui.locateOnScreen('pictures/storePos.png', confidence = 0.8)
               if(upgradePos != None):
                    pyautogui.click(upgradePos.left+30, upgradePos.top+80)
               time.sleep(100)

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
#        imgGrey = cv2q.GaussianBlur(imgGrey, (3, 3), 0)
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

        circles = np.uint16(np.around(circles))
        print("Hough transformation performed")

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
     _thread.start_new_thread(clickCookie, ())
     _thread.start_new_thread(clickUpdate, ())
     _thread.start_new_thread(clickUpgrade, ())
     # _thread.start_new_thread(getPrintscreen, ())

     with keyboard.Listener(on_press=onPress) as listenter:
          listenter.join()
