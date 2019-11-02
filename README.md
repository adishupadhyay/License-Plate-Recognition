# License-Plate-Recognition
Code tested on :
  Python version  3.6.1
  opencv-python   3.4.7+contrib
  tesserocr       2.4.0 (tesseract v4)

->Get tesserocr from here : https://github.com/simonflueckiger/tesserocr-windows_build/releases
   From the download directory, open a command prompt (simply point it to the directory that holds the ".whl" file if you opened a command    prompt from other directory). Installation via pip is done via the following code:
   
    pip install <package_name>.whl
  
  Package_name refers to the name of the whl file you have downloaded. In my case, I have downloaded 
  tesserocr-2.4.0-cp36-cp36m-win_amd64.whl. Hence, I will be using the following code for the installation:

    pip install tesserocr-2.4.0-cp36-cp36m-win_amd64.whl

->Get tesseract's language data files from here : https://github.com/tesseract-ocr/tessdata
  For English, it is "eng.traineddata"
  
->Place "eng.traineddata" inside tessdata folder. The folder should be like:

    ./tessdata :
        -configs
        -tessconfigs
        -eng.traineddata
        -eng.user-patterns
        -eng.user-words
        -info.txt
        -osd.traineddata
        -pdf.ttf

->Put the input images in "LicPlateImages" folder.

->Run Main_v1_image final.py
  Output images go in the "output" folder, thresholded images and output text is saved in the "thresimages" folder.
