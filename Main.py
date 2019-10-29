
import cv2
import numpy as np
import os
import tesserocr
from pathlib import Path

import DetectChars
import DetectPlates
import PossiblePlate

SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)

showSteps = False
path=Path('LicPlateImages')
outdict={}
namelist=[]


def main():
    blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()
    if blnKNNTrainingSuccessful == False:                               
        print("\nerror: KNN traning was not successful\n")
        return
    imgOriginalScene  = cv2.imread(str(imagepath))
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
        key=str(imagepath).split('\\')
        key=str(key[-1])
        cv2.imwrite(key, ~licPlate.imgThresh)
        os.chdir('..')
        if len(licPlate.strChars) == 0:
            print("\nno characters were detected\n\n")
            return
        drawRedRectangleAroundPlate(imgOriginalScene, licPlate)
        print("\nLicense plate read from image = " + licPlate.strChars + "\n")
        print("----------------------------------------")

        writeLicensePlateCharsOnImage(imgOriginalScene, licPlate)
        os.chdir('output')
        cv2.imwrite(key, imgOriginalScene)
        os.chdir('..')
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
    
for imagepath in path.glob("*.png"):
    if __name__ == "__main__":
        main()
#path=Path('thresimages')
#for imagepath in path.glob("*.png"):
#    tessocr()