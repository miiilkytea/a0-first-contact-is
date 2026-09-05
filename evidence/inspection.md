# Inspection record

Replace every bracketed prompt with your own observation. Keep output excerpts short.

## Part 1: First observation

**What appears to be happening?**  
In the terminal running the talker it seems to be publishing "Hello World: 'time' every second. Then in the second terminal running the listener it displays "I heard: [Hello World: 'time']." The listener starts listening  to the publisher once I start running the listener. 

**What did you observe that supports this?**  
Evidence that supports this is that after starting the publisher the listener does not start from time 0, but rather the time the publisher last published.

## Part 2: Standard demo
node list - found /listener & /talker nodes

node info /talker - found that it is publishing to /chatter, /parameter_events, and /rosout

topic list -t - displays the topics /chatter, /parameter_events, and /rosout with their types

topic info /chatter - displays topic type, number of publishers, and number of subscribers to the /chatter topic

interface show std_msgs/msg/String - displays example of string message "string data"

topic echo /chatter --once - displays the string data being published from the talker node in that moment

topic hz /chatter - displays the rate as to how often the /chatter topic is being published to

### Running nodes

**Command:** `ros2 node list`

```text
/status_monitor
/status_publisher
```

**Interpretation:** This tells me that the two nodes runnning are status_monior and status_publisher.

### Connections and message type

**Commands:**

```text
ros2 node info /status_publisher
ros2 node info /status_monitor
```

```text
(command 1)
/status_publisher
  Subscribers:

  Publishers:
    /lab0/status: std_msgs/msg/String
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log


(command 2)
/status_monitor
  Subscribers:
    /lab0/status: std_msgs/msg/String
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
  Service Servers:

```

**Interpretation:** 
The publisher is /status_publisher. The subscriber is the /status_monitor. The topic being listened and published from is /lab0/status. The message type is of type string or more specifically "std_msgs/msg/String."

### Message and rate

**Commands:**

```text
ros2 topic echo /lab0/status --once
ros2 topic hz /lab0/status
```

```text
(command line 1)
data: 'Hello World: 3117'

(command line 2)
average rate: 3.997
	min: 0.246s max: 0.254s std dev: 0.00285s window: 5


```

**Interpretation:** 
One message is "Hello World: 3117" and the approximate rate of publishing is 3.997 hz.

## Part 4: Your status system

### Nodes and topic

**Commands and relevant output:**

```text
ros2 node info /status_publisher
Subscribers:

  Publishers:
    /lab0/status: std_msgs/msg/String
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    
ros2 node info /status_monitor
/status_monitor
  Subscribers:
    /lab0/status: std_msgs/msg/String
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
```

**Interpretation:** [Explain how this supports the required node names, topic, type, publisher, and subscriber.]
This supports the required node names as the displayed nodes are both called /status_monitor and /status_publisher on the first line after getting the node info. The topics and type are verified as "/lab0/status" and "std_msgs/msg/String" in the publisher/subscriber information respectively when using the node info command.

### Message and rate

**Commands and relevant output:**

```text
ros2 topic echo /lab0/status --once
ros2 topic hz /lab0/status
```

```text
(command line 1)
data: 'Hello World: 3117'

(command line 2)
average rate: 3.997
	min: 0.246s max: 0.254s std dev: 0.00285s window: 5


```

**Interpretation:** [Explain how this supports the required message content and 4 Hz rate.]
This supports the required message content as the displayed data prints a string ans the time the message was received. The second command line output verifies the 4Hz rate as it displays the average rate as 3.997Hz.

## Part 6: Your count system

**Commands and relevant output:**

```text
[commands and output]
```

**Interpretation:** [Explain how this supports the node names, /lab0/count topic, Int32 type, publisher/subscriber connection, increasing values, and 1 Hz rate.]

## CPE 691 extension

Delete this section if you are enrolled in CPE 491.

```text
[output of ros2 topic info /lab0/status --verbose]
```

```text
[output of ros2 topic info /lab0/count --verbose]
```
