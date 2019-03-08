# A-new-and-different-network-inspire-from-SENet

Study base on [1], [2], [3] and [4] ,then modify the structure to accomplish the simulation.

## Approach 

This is a new structure inspire from SENet[[1]](http://openaccess.thecvf.com/content_cvpr_2018/papers/Hu_Squeeze-and-Excitation_Networks_CVPR_2018_paper.pdf)

<div align="center">
  <img src="https://raw.githubusercontent.com/yoyotv/Fusion-and-Extension-Netwoks/master/figures/FENet.JPG">
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

The code on other framwork(e.g. caffe, pytorch, tensorflow) will release soon.

### Paramaters

| Settings | Detail |
|:-:|:-:|
|Epoch| 200 |
|Batch| 128 |
|Initial learning rate|0.1|
|Dropout| Yes|
|Data augmentation|No|

## Try 


## References

[1] Jie Hu, Li Shen, Gang Sun; The IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2018, pp. 7132-7141 

[2] B. d’Andr ́ea-Novel, G. Bastin, and G. Campion, “Modeling andcontrol of non holonomic wheeled mobile robots,” inthe 1991 IEEEInternational Conference on Robotics and Automation, 1991, pp.1130–1135

[3] Dianwei Qian · Jianqiang Yi, "Hierarchical Sliding Mode Control for Underactuated Cranes"

[4] Xia, D.; Yao, Y.; Cheng, L. Indoor autonomous control of a two-wheeled inverted pendulum vehicle using ultra wide band technology. Sensors 2017, 17, 1401


