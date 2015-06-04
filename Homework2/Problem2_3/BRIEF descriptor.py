
# coding: utf-8

# In[17]:

import numpy as np
import math
from PIL import Image, ImageDraw
import random


givenImg = Image.open('C:\Users\Char\Downloads\\200_redCell.png', 'r').convert('LA')
#givenImg.show()
(width, height) = givenImg.size
imgData = list(givenImg.getdata())

numOfPairs = 20;
samplingPairs = makeSamplingPair(numOfPairs, width, height)
print samplingPairs

BRIEFDescriptor = makeBRIEFDescriptor(samplingPairs, numOfPairs, imgData, width, height)
print BRIEFDescriptor


# In[15]:

def makeSamplingPair(numOfPairs, width, height):
    samplingPairs = list();
    
    for i in range(numOfPairs):
        X1 = int(width*random.random());
        Y1 = int(height*random.random());
        X2 = int(width*random.random());
        Y2 = int(height*random.random());
        currSamplingPair =[[X1, Y1], [X2, Y2]]
        samplingPairs.append(currSamplingPair);
        
    return samplingPairs;


# In[11]:

def makeBRIEFDescriptor(samplingPairs, numOfPairs, imgData, width, height):
    BRIEFDescriptor = list();
    for currPair in samplingPairs:
        valueInPt1 = imgData[currPair[0][0]+width*currPair[0][1]][0];
        valueInPt2 = imgData[currPair[1][0]+width*currPair[1][1]][0];
        if(valueInPt1 > valueInPt2):
            BRIEFDescriptor.append(1);
        else:
            BRIEFDescriptor.append(0);
    
    return BRIEFDescriptor;

