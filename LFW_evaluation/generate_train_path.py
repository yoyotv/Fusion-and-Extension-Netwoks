import os
import random



data_path = '/home/dl-linux/Desktop/face_recognition/save/'

file_names=[]

for all_files in os.walk(data_path):
  file_names=all_files[2]



txt = open("train_path.txt","w")

for i in range(len(file_names)):
  txt.write(data_path+str(file_names[i])+'\n')

txt.close()
