
# coding: utf-8

# In[9]:

import numpy as np
from PIL import Image, ImageDraw


givenImg = Image.open('C:\Users\Char\Downloads\\200_redCell.png', 'r').convert('LA')
givenImg.show()




(width, height) = givenImg.size
pixels = list(givenImg.getdata())
threshold = 10
cornerList = FAST9CornerDetector(pixels, width, height, threshold)

draw = ImageDraw.Draw(givenImg)

for currCorner in cornerList:
    draw.ellipse((currCorner[0]-1, currCorner[1]-1, currCorner[0]+1, currCorner[1]+1),
                 fill=0)

givenImg.show()


# In[2]:

def FAST9CornerDetector(pixelList, width, height, threshold):
    cornerCoordList = list();
    for currX in range(width):
        for currY in range(height):
            isCorner = judgeCornerPoint(currX, currY, pixelList, width, height, threshold);
            if(isCorner == True):
                cornerCoordList.append([currX, currY]);
    
    return cornerCoordList;
            


# In[3]:

def judgeCornerPoint(currX, currY, pixelList, width, height, threshold):
    SurrondingPoints = [[currX, currY+3], [currX+1, currY+3], [currX+2, currY+2],
                        [currX+3, currY+1], [currX+3, currY], [currX+3, currY-1], [currX+2, currY-2],
                        [currX+1, currY-3], [currX, currY-3], [currX-1, currY-3], [currX-2, currY-2],
                        [currX-3, currY-1], [currX-3, currY], [currX-3, currY+1], [currX-2, currY+2],
                        [currX-1, currY+3]]
    
    brightOfCurrCoord = pixelList[currX+currY*width][0];
    continuousState = 0;
    
    for surrCoord in SurrondingPoints:
        if ((surrCoord[0] >= 0) & (surrCoord[1] >= 0) & (surrCoord[0] < width) & (surrCoord[1] < height)):
                brightOfSurrCoord = pixelList[surrCoord[0]+surrCoord[1]*width][0];
                if(continuousState >= 0):
                    if(brightOfSurrCoord > brightOfCurrCoord+threshold):
                        continuousState = continuousState+1;
                    elif(brightOfSurrCoord < brightOfCurrCoord-threshold):
                        continuousState = -1;
                    else:
                        continuousState = 0;   
                else:
                    if(brightOfSurrCoord > brightOfCurrCoord+threshold):
                        continuousState=1;
                    elif(brightOfSurrCoord < brightOfCurrCoord-threshold):
                        continuousState = continuousState-1;
                    else:
                        continuousState = 0;
                        
        if((continuousState == 9)|(continuousState == -9)):
            return True;
        
    if(continuousState > 0):
        for i in range(9-continuousState):
            surrCoord = SurrondingPoints[i]
            if ((surrCoord[0] >= 0) & (surrCoord[1] >= 0) & (surrCoord[0] < width) & (surrCoord[1] < height)):
                brightOfSurrCoord = pixelList[surrCoord[0]+surrCoord[1]*width][0];
                if(brightOfSurrCoord > brightOfCurrCoord+threshold):
                    continuousState = continuousState+1;
        
        if(continuousState == 9):
            return True;
    
    if(continuousState < 0):
        for i in range(9+continuousState):
            surrCoord = SurrondingPoints[i]
            if ((surrCoord[0] >= 0) & (surrCoord[1] >= 0) & (surrCoord[0] < width) & (surrCoord[1] < height)):
                brightOfSurrCoord = pixelList[surrCoord[0]+surrCoord[1]*width][0];
                if(brightOfSurrCoord > brightOfCurrCoord+threshold):
                    continuousState = continuousState-1;
        
        if(continuousState == -9):
            return True;
    
    return False;

