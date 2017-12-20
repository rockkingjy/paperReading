
# Depth prediction from a signle image
[14-Depth Map Prediction from a Single Image using a Multi-Scale Deep Network](https://arxiv.org/abs/1406.2283) [Code_TF](https://github.com/MasazI/cnn_depth_tensorflow)

[14-Deep convolutional neural fields for depth estimation from a single image](https://arxiv.org/abs/1411.6387) [Code_ipynb](https://github.com/asousa/DepthPrediction)

[16-Deeper Depth Prediction with Fully Convolutional Residual Networks](https://arxiv.org/abs/1606.00373) [Code TF_Matlab](https://github.com/iro-cp/FCRN-DepthPrediction)

[16-Depth from a Single Image by Harmonizing Overcomplete Local Network Predictions](https://arxiv.org/abs/1605.07081) [Code_Matlab](https://github.com/ayanc/mdepth)

[Depth Estimation by Convolutional Neural Networks](http://www.fit.vutbr.cz/study/DP/DP.php?id=18852&file=t) [Code_Caffe](https://github.com/janivanecky/Depth-Estimation)

[17-Estimated Depth Map Helps Image Classification](https://arxiv.org/abs/1709.07077) [Code](https://github.com/yihui-he/Estimated-Depth-Map-Helps-Image-Classification)


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
