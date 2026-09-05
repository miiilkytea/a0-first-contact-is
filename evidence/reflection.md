# Reflection

## From Python file to ROS graph

In 150–250 words, explain how the Python class and `main()` function relate to the running process, ROS node, publisher or subscriber, topic, and message visible in the ROS graph.

The python class and 'main()' function relate to the running process as the class sets up the bare bone instructions of the publisher or subscriber, while the main function takes that class and actually creates a new publisher or subscriber object that will create and run it. The class helps define the node name, topic name, message type, and rate of publishing or callback of that publisher or subscriber. Once the executable files are created this compiles the code and sets up the defined topic(s) that the publisher or subscriber will publish/listen to. Then in the running ROS graph the /status_publisher points into /lab0/status topic as it publishes to it, while the /status_monitor node has a arrow exiting from the /lab0/status topic as it listens from it.

## Changing the message contract

Compare your status pair with your count pair. What code changed, what stayed the same, and why must the publisher and subscriber agree on both the topic name and message type?

[Your response]

## A useful inspection command

Which command from this assignment would you try first on an unfamiliar ROS 2 system, and why?

[Your response]

## Most useful failure

Describe one failure or wrong result, the evidence that helped you locate it, and what you changed.

[Your response]

