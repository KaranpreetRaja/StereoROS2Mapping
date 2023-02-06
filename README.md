# StereoROS2Mapping
Uses a ZED 2 Stereo Camera in order to create and map out a 2D occupancy grid




## Prerequisites
### Nvidia Drivers
Install Nvidia Drivers for Ubuntu
```bash
# installed nividia drivers
sudo apt install nvidia-driver-515 nvidia-dkms-515
sudo apt upgrade
```
You need to **restart** for changes to take place
In order to test if this worked, you can run the following command
```bash
nividia-smi
```
