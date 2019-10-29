import cv2
import json
from pytesseract import image_to_string
from pathlib import Path

path=Path('images')
results={}
for imagepath in path.glob("*.png"):
      image=cv2.imread(str(imagepath))
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      results[str(imagepath)]=image_to_string(gray)

print(results)
with open('result.json', 'w') as json_file:
      json.dump(results,json_file)
