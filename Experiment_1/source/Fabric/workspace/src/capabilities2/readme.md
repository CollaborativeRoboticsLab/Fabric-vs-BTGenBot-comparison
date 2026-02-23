# Capabilities2

A reimplementation of the [capabilities](https://github.com/osrf/capabilities) package. This package is implemented using C++17 and extends the capabilities package features. 
- [capabilities2_server](./capabilities2_server/readme.md) package contains the core of the system.
- [capabilities2_runner](./capabilities2_server/readme.md) package contains base and template classes for capability implementations.


## Extentions
- [Fabric](./../fabric/readme.md) package implements a behaviour planning framework that utlizes capabilities2 system.


## System structure

![System Structure](./docs/images/system-structure.png)

## Entities

The main usage of `capabilities2` will typically involve creating or customizing capabilities through providers, interfaces and semantic interfaces. These are stored as YAML, and for more information about definitions and examples, click the links:

| Entity | Description |
| --- | --- |
| [Interfaces](./docs/interfaces.md) | The main capability specification file |
| [Providers](./docs/providers.md) | The capability provider specification file provides a mechanism to operate the capability |
| [Semantic Interfaces](./docs/semantic_interfaces.md) | The semantic interface specification file provides a mechanism to redefine a capability with semantic information |

Runners can be created using the runner API parent classes [here](./capabilities2_runner/readme.md). The capabilities service can be started using the [capabilities2_server](./capabilities2_server/readme.md) package.


## Setup Information
- [Installation](./docs/setup.md)
- [Setup Instructions with devcontainer](./docs/setup_with_dev.md)
- [Dependency installation for Fabric Runners](./docs/fabric_setup.md)
- [Dependency installation for Nav2 Runners](./docs/nav2_setup.md)
- [Dependency installation for Prompt Runners](./docs/prompt_tools_setup.md)
- [Dependency installation for Foxglove-studio](./docs/foxglove_studio.md)

## Quick Startup information

### Starting the Capabilities2 server

```bash
source install/setup.bash
ros2 launch capabilities2_server server.launch.py
```

## Additional Information
- [Motivation and Example Use Cases](./docs/motivation_and_examples.md)
- [Design Information](./docs/design.md)
- [Registering a capability](./capabilities2_server/docs/register.md)
- [Terminal based capability usage](./capabilities2_server/docs/terminal_usage.md)
- [Running test scripts](./docs/run_test_scripts.md)
- [Using with Docker](./docker/docs/startup.md)

## Acknowledgements

This work is based on the capabilities package developed by the Open Source Robotics Foundation. [github.com/osrf/capabilities](https://github.com/osrf/capabilities).
