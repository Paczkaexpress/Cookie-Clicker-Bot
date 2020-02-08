# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 22:57:30 2019

@author: Erazer
"""
from statistics import mean
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
#i = Image.open('images/numbers/y0.5.png')
#iar = np.asanyarray(i)
#
#plt.imshow(iar)
#print(iar)
#plt.show()


def threshold(imageArray):
    balanceArr = []
    newArr = imageArray
    for eachRow in imageArray:
        for eachPixel in eachRow:
            avgNum = mean(eachPixel[:2])
            balanceArr.append(avgNum)
    balance = mean(balanceArr)

#    print("balance mean: {:3}".format(balance))

    for eachRow in newArr:
        for eachPixel in eachRow:
#            print("pixel mean: {:3}".format(mean(eachPixel[:2])))
            if mean(eachPixel[:3]) > balance:
                eachPixel[0] = 255
                eachPixel[1] = 255
                eachPixel[2] = 255
            else:
                eachPixel[0] = 0
                eachPixel[1] = 0
                eachPixel[2] = 0
    return newArr

if __name__ == "__main__":

    numberOfImages = range(1,20)

    for eachImage in numberOfImages:
        imgPath = 'pictures\goldCookie\goldCookie' + str(eachImage) + '.jpg'
        img = Image.open(imgPath)
        iar = np.array(img)
        iar= threshold(iar)

        newImg = Image.fromarray(iar)

        newImgPath = 'pictures\goldCookie\goldCookie_BW_' + str(eachImage) + '.jpg'
        newImg.save(newImgPath)



