
import tesserocr
import json
from pathlib import Path


def tessocr(impath,mnm):
    namelist=[]
#    impath=key
    namelist.append(mnm)
    outdict={}
    impath = 'thresimages/'+impath    
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=0) as api:
        api.SetImageFile(impath)
        a=api.GetUTF8Text()
        if a not in namelist:
            namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=1) as api:
        api.SetImageFile(impath)
        a=api.GetUTF8Text()
        if a not in namelist:
            namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=2) as api:
        api.SetImageFile(impath)
        a=api.GetUTF8Text()
        if a not in namelist:
            namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=3) as api:
        api.SetImageFile(impath)
        a=api.GetUTF8Text()
        if a not in namelist:
            namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=4) as api:
        api.SetImageFile(impath)
        a=api.GetUTF8Text()
        if a not in namelist:
            namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=6) as api:
        api.SetImageFile(impath)
        a=api.GetUTF8Text()
        if a not in namelist:
            namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=7) as api:
        api.SetImageFile(impath)
        a=api.GetUTF8Text()
        if a not in namelist:
            namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=8) as api:
        api.SetImageFile(impath)
        a=api.GetUTF8Text()
        if a not in namelist:
            namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=9) as api:
        api.SetImageFile(impath)
        a=api.GetUTF8Text()
        if a not in namelist:
            namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=10) as api:
        api.SetImageFile(impath)
        a=api.GetUTF8Text()
        if a not in namelist:
            namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=11) as api:
        api.SetImageFile(impath)
        a=api.GetUTF8Text()
        if a not in namelist:
            namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=12) as api:
        api.SetImageFile(impath)
        a=api.GetUTF8Text()
        if a not in namelist:
            namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=13) as api:
        api.SetImageFile(impath)
        a=api.GetUTF8Text()
        if a not in namelist:
            namelist.append(api.GetUTF8Text())
    outdict[impath]=namelist
    print(namelist)
    namelist=[]
    with open(impath[:-4]+'.txt', 'w') as json_file:
        json.dump(outdict, json_file,indent=4)