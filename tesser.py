
import tesserocr
import json
from pathlib import Path

namelist=[]
outdict={}
path=Path('thresimages')
for impath in path.glob("*.png"):
    imagepath=str(impath)
    key=str(imagepath).split('\\')
    name=str(key[-1])
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=0) as api:
        api.SetImageFile(str(imagepath))
        namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=1) as api:
        api.SetImageFile(str(imagepath))
        namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=2) as api:
        api.SetImageFile(str(imagepath))
        namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=3) as api:
        api.SetImageFile(str(imagepath))
        namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=4) as api:
        api.SetImageFile(str(imagepath))
        namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=6) as api:
        api.SetImageFile(str(imagepath))
        namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=7) as api:
        api.SetImageFile(str(imagepath))
        namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=8) as api:
        api.SetImageFile(str(imagepath))
        namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=9) as api:
        api.SetImageFile(str(imagepath))
        namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=10) as api:
        api.SetImageFile(str(imagepath))
        namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=11) as api:
        api.SetImageFile(str(imagepath))
        namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=12) as api:
        api.SetImageFile(str(imagepath))
        namelist.append(api.GetUTF8Text())
    with tesserocr.PyTessBaseAPI(path='tessdata', lang='eng',psm=13) as api:
        api.SetImageFile(str(imagepath))
        namelist.append(api.GetUTF8Text())
    outdict[name]=namelist
    print(namelist)
    namelist=[]
with open('Result.txt', 'w') as json_file:
    json.dump(outdict, json_file,indent=4)
