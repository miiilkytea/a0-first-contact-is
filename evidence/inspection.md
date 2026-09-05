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

**Command:** `[command]`

```text
[relevant output]
```

**Interpretation:** [What does this tell you?]

### Connections and message type

**Commands:**

```text
[commands]
```

```text
[relevant output]
```

**Interpretation:** [Identify the publisher, subscriber, topic, and message structure.]

### Message and rate

**Commands:**

```text
[commands]
```

```text
[relevant output]
```

**Interpretation:** [Describe one message and the approximate rate.]

## Part 4: Your status system

### Nodes and topic

**Commands and relevant output:**

```text
[commands and output]
```

**Interpretation:** [Explain how this supports the required node names, topic, type, publisher, and subscriber.]

### Message and rate

**Commands and relevant output:**

```text
[commands and output]
```

**Interpretation:** [Explain how this supports the required message content and 4 Hz rate.]

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
