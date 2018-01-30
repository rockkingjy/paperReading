## Papers on self-driving cars

1712.Beyond Grand Theft Auto V for Training, Testing and Enhancing Deep Learning in Self Driving Cars

1711.CARLA: An Open Urban Driving Simulator[[Code](https://github.com/carla-simulator/carla)]: an open-source simulator for autonomous driving.

1708.Deep Steering: Learning End-to-End Driving Model from Spatial and Temporal Visual Cues

1707.Failing to Learn: Autonomously Identifying Perception Failures for Self-driving Cars

1705.Detecting Drivable Area for Self-driving Cars: An Unsupervised Approach

1703.Interpretable Learning for Self-Driving Cars by Visualizing Causal Attention

1703.Feature Analysis and Selection for Training an End-to-End Autonomous Vehicle Controller Using the Deep Learning Approach

1702.Deep Learning Algorithm for Autonomous Driving using GoogLeNet

1702.Brain Inspired Cognitive Model with Attention for Self-Driving Cars

1700.End-to-End Ego Lane Estimation based on Sequential Transfer Learning for Self-Driving Cars

1700.End-to-end Driving via Conditional Imitation Learning

1700.End-to-End Deep Reinforcement Learning for Lane Keeping Assist

1700.A vision-centered multi-sensor fusing approach to self-localization and obstacle perception for robotic cars: focus on sensor fusing.

1612.End-to-end Learning of Driving Models from Large-scale Video Datasets[[Code](https://github.com/gy20073/BDD_Driving_Model)]

1604.End to End Learning for Self-Driving Cars: nvidia's wonderful work using cnn.

1604.A Survey of Motion Planning and Control Techniques for Self-driving Urban Vehicles: A summary of these area before 2016, etter to read it first.

Awesome Autonomous Vehicles[[Github](https://github.com/takeitallsource/awesome-autonomous-vehicles)]: Papaers and resources before 2017.

## Resources

The Autonomous Driving Cookbook from Microsoft[[Code](https://github.com/Microsoft/AutonomousDrivingCookbook)]: now available for training in AirSim.

Udacity open source self-driving car programme[[Code](https://github.com/udacity/self-driving-car)]: Udacity programme, some dataset
and model available.


## Simulators

AirSim, Simulator for Drones, Cars from Micorsoft [[Code](https://github.com/Microsoft/AirSim)].

[CARLA](http://www.carla.org), An Open Urban Driving Simulator.

## Datasets

Check the table in this paper:[1612.End-to-end Learning of Driving Models from Large-scale Video Datasets](https://arxiv.org/pdf/1612.01079.pdf)

## Hierarchy of decision making system of a self-driving car 
[Reference: [1604.A Survey of Motion Planning and Control Techniques for Self-driving Urban Vehicles](https://arxiv.org/pdf/1604.07446.pdf)]

1. Route Planning: select a route from its current position to the destination.

2. Behavioral Layer: select a appropriate driving behavior at any point of time based on the conditions of the road, for example turn left, turn right, stay in lane, change-lane, stop immediately etc.

3. Motion Planning: find a trajectory after having the driving behavior command with the considerations of no collisions, comfortable for the passenger etc.

4. Local Feedback Control: execute the trajectory from motion planning by a feedback controller.

## Hardware Platform
[Nvidia DRIVER PX2 AUTOCRUISE or AUTOCHAUFFER](https://developer.nvidia.com/drive/hardware)

## Sensor Setup
### Basic:
* 1x Inertial Navigation System (GPS/IMU)
* 2x 120 FOV Forward Facing Camera
* 2x 120 FOV Side Facing Camera
* 1x 60 FOV Rear Long Range Camera
* 1x Lidar

Medium:
* 6x Radars
* 1x Thermal camera
* 1x Depth camera

Advanced:
* 1x 360 deg RGB camera
* 2x 120 FOV Blind Spot Camera
* 2x 120 FOV Front Medium Range Camera
* 2x 60 FOV Long Range Cross Traffic Camera

Reference:

https://autonomoustuff.com/product/nvidia-drive-px-on-wheels/

http://www.cvlibs.net/datasets/kitti/setup.php

## Tasks
1. Route Planning:

Localization and Mapping

Algorithms for finding a minimum-cost path

2. Behavioral Layer:

LDW - Lane Departure Warning

LKA - Lane Keep Assist

TSLR - Traffic Sign and Light Recognition

Night Vision

3. Motion Planning:

Steering Wheel Auto-control

AVM - Around View Monitor

FCW - Forward Collision Warning

BSD - Blind Spot Detection

4. Local Feedback Control:

Control System for Vehicle

5. Other tasks:

DOW - Door Open Warning

DDW - Distracted Driver Warning

## Sensors information
简单传感器：GPS，IMU, Gyroscope + accerometer: ARRIS;

视觉摄像头：精度高、可见范围远，但是害怕雾雨天；

深度摄像头：ZED(0.5~20m), Microsoft Kinect 360(Range:5m;acc:1mm at 0.5m; 4cm at 5m);

温度摄像头：Seek thermal: $500 https://www.thermal.com/compact-series.html ; Flir: http://www.flir.com/flirone/ ;

毫米波雷达：77G远程，24G近程；1000m内；不怕雾雨天，但是精度低、可见范围短；探测移动物体，静止物体效果不好。

激光雷达：精度高、可见范围远，也不怕雾雨天；Velodyne(lab use)，Quanergy、以色列Innoviz公司、德国Ibeo, etc.；

Velodyne parameters: $4000，100m, http://velodynelidar.com/vlp-16.html

2d Lidar: $500，https://www.slamtec.com/cn/Lidar

77GHz 毫米波雷达主要用在车的正前方，用于对中远距离物体的探测。

24GHz 毫米波雷达一般被安装在车后方，用于盲点检测。

视觉摄像头在自动驾驶实现预警功能，而控制的实现则离不开毫米波雷达的配合。

目前的毫米波雷达的主要缺陷在于精度还不够完美，例如无法非常精确的将两个物体进行区分，而视作一个物体的情况。只要毫米波雷达的波长、带宽足够，其成像效果也能与激光雷达相媲美，当然，实现成本也不低。而在国外，79~81GHZ 的毫米波雷达技术已进行预研阶段。

## Autonomy Levels (Five levels): [[Wikipedia](https://en.wikipedia.org/wiki/Autonomous_car#Levels_of_driving_automation)]
* Level 0 No automation;
* Level 1 (”hands on”);
* Level 2 (”hands off”);
* Level 3 (”eyes off”);
* Level 4 (”mind off”);
* Level 5 Full automation;



