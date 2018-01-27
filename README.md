
# Monocamera / RGB-D to 3D reconstruction / SLAM
[Semantic Scene Completion from a Single Depth Image](https://github.com/shurans/sscnet)

[awsome 3d reconstruction list](https://github.com/openMVG/awesome_3DReconstruction_list)

[Multi-view 3D Reconstruction via Depth Map Fusion](https://github.com/rogermm14/rec3D)

[3D Recurrent Reconstruction Neural Network](https://github.com/chrischoy/3D-R2N2)

[Dense Visual SLAM](https://vision.in.tum.de/data/software/dvo)

[Dense Continuous-Time Tracking and Mapping with Rolling Shutter RGB-D Cameras](https://vision.in.tum.de/%7ekerl/kerl_etal_iccv2015_webpage/)

[Dense Visual Odometry and SLAM (dvo_slam)](https://github.com/tum-vision/dvo_slam)

[RGB-D SLAM Dataset and Benchmark](https://vision.in.tum.de/data/datasets/rgbd-dataset)

[RTAB-Map](http://introlab.github.io/rtabmap/)

### related papers:
[16-FuseNet: Incorporating Depth into Semantic Segmentation via Fusion-based CNN Architecture](https://github.com/tum-vision/fusenet)

[Package tum_ardrone](https://github.com/tum-vision/tum_ardrone)

# Image Segmentation
[A Brief History of CNNs in Image Segmentation: From R-CNN to Mask R-CNN](https://blog.athelas.com/a-brief-history-of-cnns-in-image-segmentation-from-r-cnn-to-mask-r-cnn-34ea83205de4)

[Mask R-CNN](https://arxiv.org/abs/1703.06870)([Code](https://github.com/CharlesShang/FastMaskRCNN))

[CRF-RNN for Semantic Image Segmentation](https://github.com/torrvision/crfasrnn)


# RL
[Maze Navigation using Reinforcement Learning](https://github.com/tgangwani/GA3C-DeepNavigation)

To install simulator [DeepMind Lab](https://github.com/deepmind/lab/blob/master/docs/build.md), I've a problem of:
```
$ sudo bazel build :deepmind_lab.so --define headless=glx
INFO: Analysed target //:deepmind_lab.so (1 packages loaded).
INFO: Found 1 target...
ERROR: /home/enroutelab/Amy/lab/BUILD:988:1: C++ compilation of rule '//:deepmind_lab.so' failed (Exit 1)
python/dmlab_module.c:29:31: fatal error: numpy/arrayobject.h: No such file or directory
compilation terminated.
```
To slove this:
```
locate /arrayobject.h
```
that gave:
```
/usr/local/lib/python2.7/dist-packages/numpy/core/include/numpy/arrayobject.h
```
then change the file the python.BUILD to:
```
cc_library(
    name = "python",
    hdrs = glob([
        "include/python2.7/*.h",
        "local/lib/python2.7/dist-packages/numpy/core/include/**/*.h",
    ]),
    includes = [
        "include/python2.7",
        "local/lib/python2.7/dist-packages/numpy/core/include",
    ],
    visibility = ["//visibility:public"],
)
```
Done.

# Tensorrt customer layer implementation:
https://github.com/AastaNV/Face-Recognition

