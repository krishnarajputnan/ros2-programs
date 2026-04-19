# ros2-programs

This repository contains my ROS 2 workspace and package implementations for the AUV club recruitment tasks. 

## Prerequisites
* **OS:** Ubuntu 22.04 (Native or WSL)
* **Framework:** ROS 2 
* **Dependencies:** `colcon` build tools, Python 3 / C++

## Workspace Structure
This repository contains four main task packages:

* **`task_1_Comm_Link`**: Implements a ROS 2 chat node using publisher and subscriber mechanics for communication.
* **`task2_signalprocessing`**: [Add a 1-sentence description of what your code does here]
* **`task3_deadreck`**: Implementation for dead reckoning and bot pose estimation.
* **`task4_visual_lock`**: [Add a 1-sentence description of the visual processing goal here]

---

## Setup and Build Instructions

To test these packages on your local machine, follow these steps:

**1. Clone the repository**
```bash
git clone https://github.com/krishnarajputnan/ros2-programs
cd ros2-programs
```

**2. Build the workspace**
Ensure you are in the root directory containing the task packages, then compile the code using `colcon`:
```bash
colcon build
```

**3. Source the workspace**
To make the newly built packages visible to your ROS 2 environment, source the setup file:
```bash
source install/setup.bash
```
*(Note: You will need to run this source command in every new terminal window you open).*

---

## Running the Nodes

Below are the commands to execute the nodes for each specific task. 

### Task 1: Comm-Link
To test the chat nodes, you will need two separate terminal windows. Remember to run `source install/setup.bash` in both.

**Terminal 1 (Run the Publisher):**
```bash
ros2 run comm_link chat_node <name_of_your_publisher_executable>
```

**Terminal 2 (Run the Subscriber):**
```bash
ros2 run comm_link chat_node <name_of_your_subscriber_executable>
```

### Task 2: Signal Processing
**Terminal 1 (Run the publisher):**
```bash
ros2 run auv_signal_processing publisher
```
**Terminal 2 (Run the processor):**
```bash
ros2 run auv_signal_processing processor
```

**Terminal 3 (Run the output):**
```bash
ros2 run auv_signal_processing output
```

### Task 3: Dead Reckoning
**Terminal 1 (Run the commander):**
```bash
ros2 run sub_controller commander
```
**Terminal 2 (Run the navigator):**
```bash
ros2 run sub_controller navigator
```

### Task 4: Visual Lock
```bash
ros2 run task4_vision visual_lock
```
I was not able to access webcam from WSL, so i used a dummy webcam simulation.
