# StereoROS2Mapping
Uses a ZED 2 Stereo Camera in order to create and map out a 2D occupancy grid




## Prerequisites



### Nvidia Drivers
The code snippet below Install Nvidia Drivers for Linux
```bash
# installs nividia drivers
$ sudo apt install nvidia-driver-515 nvidia-dkms-515
$ sudo apt upgrade
```
In order to test if this worked, you can run the following command
```bash
$ nividia-smi
```
### Install CUDA for Linux
```bash
# This is the CUDA installation script for CUDA 12.0.1 for device running Ubuntu 22.04 with a x86_64 archetecture
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
$ sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
$ wget https://developer.download.nvidia.com/compute/cuda/12.0.1/local_installers/cuda-repo-ubuntu2204-12-0-local_12.0.1-525.85.12-1_amd64.deb
$ sudo dpkg -i cuda-repo-ubuntu2204-12-0-local_12.0.1-525.85.12-1_amd64.deb
$ sudo cp /var/cuda-repo-ubuntu2204-12-0-local/cuda-*-keyring.gpg /usr/share/keyrings/
$ sudo apt-get update
$ sudo apt-get -y install cuda
```
For your own custom device, please install the correct latest version of CUDA from the link below:
https://developer.nvidia.com/cuda-downloads?



You need to restart your system for changes to take place:
```bash
$ sudo reboot
```