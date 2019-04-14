from PIL import Image
import numpy as np
import time
import keras
from align import AlignDlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import dlib


which_line=0





def evaluate_genarator(which_line):
    with open('/home/dl-linux/Desktop/face_recognition/pairs.txt') as file:
      all_line=file.readlines()
    file.close()
    #print all_line[which_line]
    index = all_line[which_line].split('\t')
    if len(index) == 3 :
          image1=cv2.imread('/home/dl-linux/Desktop/face_recognition/'+'lfw_custom/'+index[0]+'/'+index[1]+'.jpg', 1)
          image1=image1[...,::-1]
          image2=cv2.imread('/home/dl-linux/Desktop/face_recognition/'+'lfw_custom/'+index[0]+'/'+index[2][:-1]+'.jpg', 1)
          image2=image2[...,::-1]
          label=1
    else:
          image1=cv2.imread('/home/dl-linux/Desktop/face_recognition/'+'lfw_custom/'+index[0]+'/'+index[1]+'.jpg', 1)
          image1=image1[...,::-1]
          image2=cv2.imread('/home/dl-linux/Desktop/face_recognition/'+'lfw_custom/'+index[2]+'/'+index[3][:-1]+'.jpg', 1)
          image2=image2[...,::-1]
          label=0
          


    #print(d)
    image1 = np.expand_dims(image1,axis = 0)
    image2 = np.expand_dims(image2,axis = 0)

    #print image1.shape
    #print image2.shape

    return  image1,image2,label





#evaluate_genarator(which_line)

