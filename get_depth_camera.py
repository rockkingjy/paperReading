#!/usr/bin/env python
# Master's Thesis - Depth Estimation by Convolutional Neural Networks
# Jan Ivanecky; xivane00@stud.fit.vutbr.cz

from __future__ import print_function	
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image
import cv2
#import cv
import os.path
os.environ['GLOG_minloglevel'] = '2' 
import caffe
import scipy.ndimage
import argparse
import operator	
import shutil

WIDTH = 298
HEIGHT = 218
OUT_WIDTH = 74
OUT_HEIGHT = 54
GT_WIDTH = 420
GT_HEIGHT = 320


def testNet(net, img):	
    net.blobs['X'].data[...] = img	
    net.forward()
    output = net.blobs['depth-refine'].data
    output = np.reshape(output, (1,1,OUT_HEIGHT, OUT_WIDTH))
    return output
    
def loadImage(path, channels, width, height):
    img = caffe.io.load_image(path)
    img = caffe.io.resize(img, (height, width, channels))
    img = np.transpose(img, (2,0,1))
    img = np.reshape(img, (1,channels,height,width))
    return img

def printImage(img, name, channels, width, height):
    params = list()
    #params.append(cv.CV_IMWRITE_PNG_COMPRESSION)
    params.append(8)

    imgnp = np.reshape(img, (int(height), int(width), int(channels)))
    imgnp = np.array(imgnp * 255, dtype = np.uint8)
    cv2.imwrite(name, imgnp, params)


def ProcessToOutput(depth):
    depth = np.clip(depth, 0.001, 1000)	
    return np.clip(2 * 0.179581 * np.log(depth) + 1, 0, 1)
            
# args
parser = argparse.ArgumentParser()
parser.add_argument('--log', action='store_true', default=False)
args = parser.parse_args()
# models
caffemodel = "model/model_norm_abs_100k.caffemodel"
deployfile = "model/model_norm_abs_100k.prototxt"
caffe.set_mode_gpu()
net = caffe.Net(deployfile, caffemodel, caffe.TEST)
# camera
cap = cv2.VideoCapture(0)
print(cap)
cap.set(3,WIDTH)
cap.set(4,HEIGHT)
# main loop
while(True):
    
    ret, frame = cap.read()
    print('Read a new frame: ',ret)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cv2.imwrite("tempImage.jpg",frame)
    input = loadImage("tempImage.jpg", 3, WIDTH, HEIGHT)
    input *= 255
    input -= 127

    output = testNet(net, input)
    outWidth = OUT_WIDTH
    outHeight = OUT_HEIGHT
    scaleW = float(GT_WIDTH) / float(OUT_WIDTH)
    scaleH = float(GT_HEIGHT) / float(OUT_HEIGHT)
    output = scipy.ndimage.zoom(output, (1,1,scaleH,scaleW), order=3)
    outWidth *= scaleW
    outHeight *= scaleH

    input += 127
    input = input / 255.0
    input = np.transpose(input, (0,2,3,1))
    input = input[:,:,:,(2,1,0)]
    output = ProcessToOutput(output)

    cv2.imshow('input',input)
    cv2.imshow('output',output)


cap.release()    
cv2.destroyAllWindows()