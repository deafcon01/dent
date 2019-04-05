import os
import cv2
#from json2xml import json2xml,readfromjson
cdir=os.getcwd()
outdir='clahe/'

if not os.path.exists(os.path.join(cdir,outdir)):
    os.mkdir(outdir)
for files in os.listdir(os.path.join(cdir,'train/images')):
    bgr = cv2.imread(os.path.join(cdir,'train/images',files))
    lab = cv2.cvtColor(bgr,cv2.COLOR_BGR2LAB)
    lab_planes = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(16,16))
    lab_planes[0]=clahe.apply(lab_planes[0])
    lab = cv2.merge(lab_planes)
    bgr = cv2.cvtColor(lab,cv2.COLOR_LAB2BGR)
    cv2.imwrite(outdir+files,bgr)

