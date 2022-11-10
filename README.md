# navsatfix_trajectory

**This package shows trajectory by a NavSatFix topic**

## Requirement
+ Ubuntu 18.04
+ ROS (Melodic)
+ Python 2.7.x

## Set Up
Download `navsatfix_trajectory` package.

```shell
$ cd ~/catkin_ws/src/
$ git clone https://github.com/HHorimoto/navsatfix_trajectory.git
$ cd ~/catkin_ws
$ catkin_make
```

## How To Use

1. Place your rosbag in this package's bags folder and check it if it is in bags folder by following command.

```shell
$ roscd navsatfix_trajectory/bags/
$ ls
rosbag.bag
```


2. Launch `navsatfix_trajectory` launch file. I belive that you need to specify your bag name with comand line.

```shell
$ roslaunch navsatfix_trajectory navsatfix_trajectory.launch bag_name:=your_bag_name
```

### Main Parameters

+ ***bag_name*** : rosbag name you placed.
    default : `rosbag`

+ ***navsatfix_topic*** : a NavSatFix topic name. 
    default : `fix`
