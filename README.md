# \# ros2-programs



This repository contains my ROS 2 workspace and package implementations for the AUV club recruitment tasks. 



\## Prerequisites

\* \*\*OS:\*\* Ubuntu 22.04 (Native or WSL)

\* \*\*Framework:\*\* ROS 2 

\* \*\*Dependencies:\*\* `colcon` build tools, Python 3 / C++



\## Workspace Structure

This repository contains four main task packages:



\* \*\*`task\_1\_Comm\_Link`\*\*: Implements a ROS 2 chat node using publisher and subscriber mechanics for communication.

\* \*\*`task2\_signalprocessing`\*\*: \[Add a 1-sentence description of what your code does here]

\* \*\*`task3\_deadreck`\*\*: Implementation for dead reckoning and bot pose estimation.

\* \*\*`task4\_visual\_lock`\*\*: \[Add a 1-sentence description of the visual processing goal here]



\---



\## Setup and Build Instructions



To test these packages on your local machine, follow these steps:



\*\*1. Clone the repository\*\*

```bash

git clone <paste-your-github-repo-link-here>

cd <name-of-the-cloned-folder>

```



\*\*2. Build the workspace\*\*

Ensure you are in the root directory containing the task packages, then compile the code using `colcon`:

```bash

colcon build

```



\*\*3. Source the workspace\*\*

To make the newly built packages visible to your ROS 2 environment, source the setup file:

```bash

source install/setup.bash

```

\*(Note: You will need to run this source command in every new terminal window you open).\*



\---



\## Running the Nodes



Below are the commands to execute the nodes for each specific task. 



\### Task 1: Comm-Link

To test the chat nodes, you will need two separate terminal windows. Remember to run `source install/setup.bash` in both.



\*\*Terminal 1 (Run the Publisher):\*\*

```bash

ros2 run comm\_link <name\_of\_your\_publisher\_executable>

```



\*\*Terminal 2 (Run the Subscriber):\*\*

```bash

ros2 run comm\_link <name\_of\_your\_subscriber\_executable>

```



\### Task 2: Signal Processing

```bash

ros2 run <task2\_package\_name> <task2\_executable\_name>

```



\### Task 3: Dead Reckoning

```bash

ros2 run <task3\_package\_name> <task3\_executable\_name>

```



\### Task 4: Visual Lock

```bash

ros2 run <task4\_package\_name> <task4\_executable\_name>

```

