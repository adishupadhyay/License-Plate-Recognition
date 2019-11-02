
import cv2
import numpy as np
import os
import tesserocr
from pathlib import Path

import DetectChars
import DetectPlates
import PossiblePlate
import tesser

SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)

showSteps = False
path=Path('LicPlateImages')

def main():
    licno=0
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()
        if blnKNNTrainingSuccessful == False:                               
            print("\nerror: KNN traning was not successful\n")
            return
        
        imgOriginalScene  = frame                           ## for video   
        cv2.imshow('video', imgOriginalScene)
        platename='video'+str(licno)+'.png' 
                       
#        imgOriginalScene  = cv2.imread(str(imagepath))                      ## for image
#        platename=str(imagepath).split('\\')
#        platename=str(platename[-1])
        
        if imgOriginalScene is None:
            print("\nerror: image not read from file \n\n")
            os.system("pause")
            return
        listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)
        listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)
        if len(listOfPossiblePlates) == 0:
            print("\nno license plates were detected\n")
        else:
            listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)
            licPlate = listOfPossiblePlates[0]
            os.chdir('thresimages')
            cv2.imwrite(platename, ~licPlate.imgThresh)
            os.chdir('..')
            tesser.tessocr(platename,licPlate.strChars)
            
            if len(licPlate.strChars) == 0:
                print("\nno characters were detected\n\n")
    #                return
            drawRedRectangleAroundPlate(imgOriginalScene, licPlate)
            print("\nLicense plate read from image = " + licPlate.strChars + "\n")
            print("----------------------------------------")
            writeLicensePlateCharsOnImage(imgOriginalScene, licPlate)
            os.chdir('output')
            cv2.imwrite(platename, imgOriginalScene)
            os.chdir('..')
            licno=licno+1
            cv2.imshow('video', imgOriginalScene)                          ##Uncomment this block for video
        if cv2.waitKey(1) & 0xFF == ord('q'):                              ##
            cap.release()                                                  ##
            cv2.destroyAllWindows()                                        ##
            break                                                          ##Uncomment this block for video
    return

def drawRedRectangleAroundPlate(imgOriginalScene, licPlate):
    p2fRectPoints = cv2.boxPoints(licPlate.rrLocationOfPlateInScene)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), SCALAR_RED, 2)
    
def writeLicensePlateCharsOnImage(imgOriginalScene, licPlate):
    ptCenterOfTextAreaX = 0                             
    ptLowerLeftTextOriginX = 0                          
    ptLowerLeftTextOriginY = 0
    sceneHeight, sceneWidth, sceneNumChannels = imgOriginalScene.shape
    plateHeight, plateWidth, plateNumChannels = licPlate.imgPlate.shape
    intFontFace = cv2.FONT_HERSHEY_SIMPLEX
    fltFontScale = float(plateHeight) / 30.0
    intFontThickness = int(round(fltFontScale * 1.5))
    textSize, baseline = cv2.getTextSize(licPlate.strChars, intFontFace, fltFontScale, intFontThickness)
    ( (intPlateCenterX, intPlateCenterY), (intPlateWidth, intPlateHeight), fltCorrectionAngleInDeg ) = licPlate.rrLocationOfPlateInScene
    intPlateCenterX = int(intPlateCenterX)
    intPlateCenterY = int(intPlateCenterY)
    ptCenterOfTextAreaX = int(intPlateCenterX)
    if intPlateCenterY < (sceneHeight * 0.75):
        ptCenterOfTextAreaY = int(round(intPlateCenterY)) + int(round(plateHeight * 1.6))
    else:
        ptCenterOfTextAreaY = int(round(intPlateCenterY)) - int(round(plateHeight * 1.6))
    textSizeWidth, textSizeHeight = textSize
    ptLowerLeftTextOriginX = int(ptCenterOfTextAreaX - (textSizeWidth / 2))
    ptLowerLeftTextOriginY = int(ptCenterOfTextAreaY + (textSizeHeight / 2))
    cv2.putText(imgOriginalScene, licPlate.strChars, (ptLowerLeftTextOriginX, ptLowerLeftTextOriginY), intFontFace, fltFontScale, SCALAR_YELLOW, intFontThickness)
    
#for imagepath in path.glob("*.png"):        #### Comment this line for video
if __name__ == "__main__":              #### Unindent this block for video
    main()
