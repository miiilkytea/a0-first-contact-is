# Reflection

## From Python file to ROS graph

In 150–250 words, explain how the Python class and `main()` function relate to the running process, ROS node, publisher or subscriber, topic, and message visible in the ROS graph.

The python class and 'main()' function relate to the running process as the class sets up the bare bone instructions of the publisher or subscriber, while the main function takes that class and actually creates a new publisher or subscriber object that will create and run it. The class helps define the node name, topic name, message type, and rate of publishing or callback of that publisher or subscriber. Once the executable files are created this compiles the code and sets up the defined topic(s) that the publisher or subscriber will publish/listen to. Then in the running ROS graph the /status_publisher points into /lab0/status topic as it publishes to it, while the /status_monitor node has a arrow exiting from the /lab0/status topic as it listens from it.

## Changing the message contract

Compare your status pair with your count pair. What code changed, what stayed the same, and why must the publisher and subscriber agree on both the topic name and message type?

The code that changed when comparing the status and the count pairs is the message type changed for the import and when setting their types for the publisher & subscriber declarations. Additionally, another important piece of code that changed was the %s to %d when printing the publisher and subscriber data. This changed due to the message type changing from string to integer. The code that stayed the same between the status pair and count pair was the overall behavior and the main function. 

The publisher and subscriber must agree on both the topic and message type because in order for both to talk/listen to one another they must be on the same topic and must be talking/listening to the same data type. It is similar to a radio station: if I am on a different radio station than my preferred music station, then I will not hear any music. Likewise, if I am on a radio station, but it's playing a foreign language I will not understand them. The same applies for topics and message types, where the topic is like the radio station and the message type is like the preferred language: both must be the same in order for them to communicate.

## A useful inspection command

Which command from this assignment would you try first on an unfamiliar ROS 2 system, and why?

I would use the "ros2 node list" or "ros2 topic list -t" command in order to understand an unfamiliar ROS 2 system. I would use the node list command because it will tell me what nodes are running at that given moment. Additionally, I would use topic list -t because it would give me a better understanding of what topics the nodes might be publishing to in addition to their types.

## Most useful failure

Describe one failure or wrong result, the evidence that helped you locate it, and what you changed.

One useful failure I experienced within this project was when running the count_monitor.py program. After editing the code to adapt it from a string to an integer I ran it but nothing was being listened to. The terminal stayed blank on a new line. With this behavior I knew that the program was running correctly; however, the count_monitor was not listening to the count_publisher. With this understanding I needed to check the topic the count_monitor was listening to. By doing this check I realized I had the count_monitor listening to /lab0/status rather than /lab0/count. After changing the count_monitor to the correct topic the program then listened in on the publisher correctly. 

