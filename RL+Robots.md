## RL
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
