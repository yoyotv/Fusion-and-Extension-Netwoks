from PIL import Image
import numpy as np
import time
import keras
from align import AlignDlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import dlib

#batch_size = 64


train_txt_path = '/home/dl-linux/Desktop/face_recognition/train_path.txt'



def training_genarator(train_txt_path,batch_size):
  while True:
    with open(train_txt_path) as file:
      print 'HI'
      for line in file:
        index = line.split('/')
        file_name = index[-1]
        file_class_and_ori_index = file_name.split('_')

        image=cv2.imread(line[:-1], 1)
        image=image[...,::-1]




        #image_ori = image
########################
        #image,bb = align_image(image)

        #image = (image/255.).astype(np.float32)
########################
        #plt.imshow(image_ori)

        #plt.gca().add_patch(patches.Rectangle((bb.left(), bb.top()), bb.width(), bb.height(), fill=False, color='red'))
        #plt.show()   


        #time.sleep(1)



        #a=Image.fromarray(x)       show the picture
        #a.show()


        x = np.expand_dims(image,axis = 0)
        if len(x.shape) != 4:
            x = np.expand_dims(x,axis = 3)
            x=np.concatenate([x,np.zeros((1,250,250,1)),np.zeros((1,250,250,1))],axis=3)

        y = np.array(file_class_and_ori_index[0])
        y = np.expand_dims(y,axis = 0)


        try:
          inputs
        except NameError:
          inputs = x
        else:
          inputs = np.append(inputs,x,axis=0)

        try:
          labels
        except NameError:
          labels = y
        else:
          labels = np.append(labels,y,axis=0)



        if inputs.shape[0]==batch_size:

          input_data = inputs
          output_data = keras.utils.to_categorical(labels,10575)
          #print input_data.shape
          #print output_data.shape
          del inputs
          del labels
          yield input_data, output_data



#training_genarator(train_txt_path,batch_size)

