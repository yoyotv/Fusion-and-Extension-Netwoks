import os
import numpy
from PIL import Image
import time
import cv2
import dlib
from align import AlignDlib
import time
import numpy as np

data_path = '/home/dl-linux/Desktop/face_recognition/CASIA-maxpy-clean/'
data_save_path = '/home/dl-linux/Desktop/face_recognition/save/'



if not os.path.isdir(data_save_path):
    os.makedirs(data_save_path)


alignment = AlignDlib('models/landmarks.dat')

def align_image(img):
  bb=alignment.getLargestFaceBoundingBox(img)
  if bb is None:
    #print 'OMG'
    bb = dlib.rectangle(int(46),int(47),int(201),int(202))
  #print 'bb:'+ str(type(bb))
  return alignment.align(250, img, bb,landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE),bb

i=0
for folders in sorted(os.listdir(data_path)):
  print folders
  j=1
  for each_file in sorted(os.listdir(data_path + folders)):
    #image = Image.open(data_path + folders + '/' + each_file)

    image=cv2.imread(data_path + folders + '/' + each_file, 1)
    image=image[...,::-1]

    #time.sleep(1)
    image,bb = align_image(image)

#(data_save_path+str(i)+'_'+str(j),'JPEG')
    image=image[...,::-1]

    cv2.imwrite(data_save_path+str(i)+'_'+str(j) + '.jpg',image)
    j=j+1
  print 'Finish: ' + str(i)
  i=i+1



