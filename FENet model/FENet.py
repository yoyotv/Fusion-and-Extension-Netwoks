import tensorflow as tf
import keras
from keras.layers import Conv2D, BatchNormalization, Activation
from keras.layers import AveragePooling2D, Input, Flatten,Reshape,multiply

def fe_block(input):
  init = input
  hw = int(input.shape[1])
  filternum = int(input.shape[3])
  fe = Reshape((filternum,hw,hw))(init)
  fe = AveragePooling2D(pool_size=(filternum,1), strides=(1,1), padding='valid')(fe)
  fe = Reshape((hw, hw, 1))(fe)
  fe = Conv2D(1, (hw, hw), padding='same')(fe)
  fe = Activation('sigmoid')(fe)
  fe = Reshape((hw, hw,1))(fe)
  fe_output = multiply([init,fe])
  
  return fe_output
