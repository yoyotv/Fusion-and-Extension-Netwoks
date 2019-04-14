import numpy as np
import generator_lfw
import keras
from keras.models import load_model
import time
from keras.models import Model

threshold=np.arange(1.4,1.7,0.1)

def cosine_similarity(input1,input2):

  input1 = np.reshape(input1,(input1.shape[-1]))
  input2 = np.reshape(input2,(input2.shape[-1]))
  #print "1234"
  #print np.dot(input1,input2)
  #print (np.linalg.norm(input1)*np.linalg.norm(input2))
  #print np.arccos(np.dot(input1,input2)/(np.linalg.norm(input1)*np.linalg.norm(input2)))

  return np.arccos(np.dot(input1,input2)/(np.linalg.norm(input1)*np.linalg.norm(input2)))

def answer_is_correct_or_not(answer,truth,correct_number):
  if answer == truth:
    correct_number=correct_number+1
  return correct_number



evaluation_index=1




#model=load_model('saved_models/20/ResNet20v1_model.012.h5')
model=load_model('saved_models/ResNet20v1_se_model.012.h5')
model.summary()
model.layers.pop()


best_accuracy = 0
best_threshold = 0
#print d

"""
for t in threshold:

  count = 0
  correct_number=0
  for i in range(0,6000):
    print 'Process: ' + ' Threshold ' + str(t) + ', ' + str(count) + '/5400'
    if i >= evaluation_index*600 and i < evaluation_index*600+600:
      pass
    else:

      which_line = i
      image1,image2,truth=generator_lfw.evaluate_genarator(which_line)


      features_model = Model(inputs=model.input,output=model.get_layer('dense_1').output)
      #features_model = Model(inputs=model.input,output=model.get_layer('flatten_1').output)

      output1 = features_model.predict(image1)
      output2 = features_model.predict(image2)


      if cosine_similarity(output1,output2)>t:
        answer=0
      else:
        answer=1

      #print t
      #print answer
      #print truth
      #print correct_number

      #time.sleep(5)
      correct_number = answer_is_correct_or_not(answer,truth,correct_number)
      #print i
      #print correct_number
      count=count+1 


  accuracy = correct_number / (5400.0)

  if accuracy > best_accuracy:
    best_accuracy = accuracy
    best_threshold = t

  print 'The accuracy of Threshold ' + str(t) + ' is :' + str(accuracy)
  txt = open("result.txt","a")
  txt.write('The accuracy of Threshold ' + str(t) + ' is :' + str(accuracy)+'\n')
  txt.close()

print
print 'The best accuracy is: ' + str(best_accuracy) + ' at Threshold : ' + str(best_threshold) 
txt = open("result.txt","a")
txt.write('\n')
txt.write('The best accuracy is: ' + str(best_accuracy) + ' at Threshold : ' + str(best_threshold))
txt.close()

"""

##############################
best_threshold=1.4
correct_number=0
for evaluation_index in range(0,10):
 print evaluation_index
 correct_number=0
 for i in range(evaluation_index*600,evaluation_index*600+600):
      which_line = i
      image1,image2,truth=generator_lfw.evaluate_genarator(which_line)


      features_model = Model(inputs=model.input,output=model.get_layer('dense_7').output)
      output1 = features_model.predict(image1)
      output2 = features_model.predict(image2)

      #print output1.shape
      #print output2.shape
      #print distance(output1,output2)
      #print t




      #time.sleep(5)
      if cosine_similarity(output1,output2)>best_threshold:
        answer=0
      else:
        answer=1
      #print answer
      correct_number = answer_is_correct_or_not(answer,truth,correct_number)
      #print i
      #print correct_number


 accuracy = correct_number / (600.0)
 txt = open("result.txt","a")
 txt.write('The performance of evaluation_index '+ str(evaluation_index) + ' is ' + str(accuracy) + ' at Threshold : ' + str(best_threshold))
 txt.close()





