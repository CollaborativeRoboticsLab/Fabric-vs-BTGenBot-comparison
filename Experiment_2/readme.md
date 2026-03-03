# Experiment 2

## Setup

Clone this repo and then

To setup Fabric follow instructions in [Experiment_2/source/fabric](./workspace/src/fabric/readme.md)
To setup Capabilities2 follow instructions in [Experiment_2/source/capabilities2](./workspace/src/capabilities2/readme.md)
To setup PromptTools follow instructions in [Experiment_2/source/prompt_tools](./workspace/src/prompt_tools/README.md)
To setup Perception follow instructions in [Experiment_2/source/perception](./workspace/src/perception/readme.md)

After that, select a plan in `fabric/fabric/config/fabric.yaml`.

## Build

```bash
cd Experiment_2/workspace
colcon build
```

## Run 

Then run following commands one after the other on different terminals

```bash
export OPENAI_API_KEY=
source install/setup.bash
ros2 launch perception server.launch.py
```

```bash
export OPENAI_API_KEY=
source install/setup.bash
ros2 launch prompt_bridge prompt_bridge.launch.py
```

```bash
source install/setup.bash
ros2 launch capabilities2_server capabilities2_server.launch.py
```

```bash
source install/setup.bash
ros2 launch fabric fabric.launch.py
```