# Author: Karanpreet Raja
# This the installation shell script for everything you need in order to use this ROS2 code in order to get the stero camera working



# installed nividia drivers
sudo apt install nvidia-driver-515 nvidia-dkms-515
sudo apt upgrade
# you need to restart for changes to take place
# in order to test if this worked, do `nividia-smi`


# install nvidia cuda toolkit
sudo apt-get install nvidia-cuda-toolkit



cd ~/Downloads


# For another version, get the updated link from the following: https://www.stereolabs.com/developers/release/ 
wget https://download.stereolabs.com/zedsdk/3.8/cu117/ubuntu22 



# CUDA Install:
# Replace following block for your machine from https://developer.nvidia.com/cuda-downloads?
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.0.1/local_installers/cuda-repo-ubuntu2204-12-0-local_12.0.1-525.85.12-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2204-12-0-local_12.0.1-525.85.12-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-12-0-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda


# install the zed sdk
sudo apt install zstd
chmod +x ZED_SDK_Ubuntu22_cuda11.7_v3.8.2.zstd.run
./ZED_SDK_Ubuntu22_cuda11.7_v3.8.2.zstd.run




#Now that Installation Is done, Reboot
sudo reboot




sudo apt install python3-rosdep2

$ cd ~/ros2_ws/src/ #use your current ros2 workspace folder
$ git clone  --recursive https://github.com/stereolabs/zed-ros2-wrapper.git
$ cd ..
$ rosdep install --from-paths src --ignore-src -r -y
$ colcon build --symlink-install --cmake-args=-DCMAKE_BUILD_TYPE=Release
$ echo source $(pwd)/install/local_setup.bash >> ~/.bashrc
$ source ~/.bashrc

