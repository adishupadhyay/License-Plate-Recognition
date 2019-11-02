import re
import tesserocr
import json
from pathlib import Path


def tessocr(impath,mnm):
    namelist=[]
#    impath=key
    namelist.append(mnm)
    outdict={}
    impath = 'thresimages/'+impath    
    for i in (7,8,9,10,13):
        with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=i) as api:
            api.SetImageFile(impath)
            a=api.GetUTF8Text()
            namelist.append(re.sub('\W+','', a))
            print(namelist)
            outdict[i]=namelist
            namelist=[]
    with open(impath[:-4]+'.txt', 'w') as json_file:
        json.dump(outdict, json_file,indent=4)