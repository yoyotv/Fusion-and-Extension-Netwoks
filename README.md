# Fusion-and-Extension-Netwoks

This is a new and useful convolutional neural network inspired by SENet[[1]](http://openaccess.thecvf.com/content_cvpr_2018/papers/Hu_Squeeze-and-Excitation_Networks_CVPR_2018_paper.pdf) and "Cerebellar model articulation controller"[[2]](https://ws680.nist.gov/publication/get_pdf.cfm?pub_id=820151).

## Approach 

<div align="center">
  <img src="https://github.com/yoyotv/Fusion-and-Extension-Netwoks/blob/master/figures/FENet.JPG?raw=true">
</div>
<p align="center">
  Figure 1: Diagram of a Fusion-and-Extension building block.
</p>

<div align="center">
   <img src="https://raw.githubusercontent.com/yoyotv/Fusion-and-Extension-Netwoks/master/figures/SE-ResNet-module.jpg" width="420" height="500">
  <img src="https://raw.githubusercontent.com/yoyotv/Fusion-and-Extension-Netwoks/master/figures/FE-ResNet-module.JPG"  width="450" height="500">
</div>
<p align="center">
  Figure 2: Schema of SE-Net and FE-Net modules.
</p>


## GET started

Success in :

python 2.7,  keras 2.2.4

I implement it on keras.

The code on other framworks(e.g. caffe, pytorch, tensorflow) will be released soon.

### Paramaters

| Settings | Detail |
|:-:|:-:|
|Epoch| 200 |
|Batch| 128 |
|Initial learning rate|0.1|
|Dropout| Yes|
|Data augmentation|No|

## Try 

Call the "fe_block" function and insert it into the base framework.

## Results

I evaluate the model on CIFAR10/100 and LFW Face identification dataset.

<div align="center">
   <img src="https://raw.githubusercontent.com/yoyotv/Fusion-and-Extension-Netwoks/22a6c7c7e82d7fe52ef93ea247de873101b088c4/figures/c10.jpg" width="430" height="650">
  <img src="https://raw.githubusercontent.com/yoyotv/Fusion-and-Extension-Netwoks/22a6c7c7e82d7fe52ef93ea247de873101b088c4/figures/c100.jpg"  width="440" height="650">
</div>
<p align="center">
  Figure 3: Results of CIFAR10 and CIFAR100.
</p>

## References

[1] Jie Hu, Li Shen, Gang Sun, "Squeeze-and-Excitation Networks" ; The IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2018, pp. 7132-7141 

[2] J.S. Albus (1975). "A New Approach to Manipulator Control: the Cerebellar Model Articulation Controller (CMAC)". In: Trans. ASME, Series G. Journal of Dynamic Systems, Measurement and Control, Vol. 97, pp. 220–233, 1975.



