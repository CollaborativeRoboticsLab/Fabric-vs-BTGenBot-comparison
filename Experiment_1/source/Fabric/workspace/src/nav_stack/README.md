# Navigation Stack

### Install dependencies

```bash
sudo apt install ros-$ROS_DISTRO-navigation2 ros-$ROS_DISTRO-nav2-bringup ros-$ROS_DISTRO-slam-toolbox
```

### Clone the package

```bash
mkdir -p navstack_ws/src
cd navstack_ws/src
```

```bash
cd ..
rosdep install --from-paths src -y --ignore-src
```


### Build the package
```bash
colcon build
```

## Launch Nav2 with SLAM Toolbox

```bash
source install/setup.bash
ros2 launch nav_stack system.launch.py
```
