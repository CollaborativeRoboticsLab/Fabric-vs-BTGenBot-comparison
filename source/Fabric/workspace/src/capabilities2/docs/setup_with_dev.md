## Using Capabilities package (Development and Deployment)

The current package has been tested on Ubuntu and ROS2 Humble, Rolling and Jazzy. Complete following sections in order.

### Base folder creation

Create the workspace folder by running following commands in the terminal.

```bash
mkdir -p /home/$USER/capabilities_ws/src
cd /home/$USER/capabilities_ws/src
```

### Compile

Use colcon to build the packages:

```bash
colcon build
```
