# Documentation trail

Use the two official ROS 2 Jazzy source files linked in Part 3. Quote only the short line or fragment needed to identify each element.

| Code element | File and line or short fragment | What this element does |
|---|---|---|
| Import the message type | [from std_msgs.msg import String] | [imports the standard string message type] |
| Assign the node name | [super().__init__('minimal_subscriber')] | [This line initializes a new node and names it based on what is given in parameter] |
| Create the publisher | [self.publisher_ = self.create_publisher(String, 'topic', 10)] | [creates a new publisher setting the datatype being sent, the topic, and que size] |
| Create the subscription | [self.subscription = self.create_subscription (...)] | [Creates a new subscriber setting data type, topic, what it'll display, que size] |
| Assign the topic name | [self.publisher_ = self.create_publisher(String, 'topic', 10)] | [In the parameters of the creating a publisher, the topic name is set] |
| Control when a callback occurs | [timer_period = 0.5] | [sets the time period for the callback to 0.5s] |
| Initialize, run, and shut down ROS | [publisher_member_function.py | lines 38-49] | [Within the main function initializes a new publisher object using the created class, starts running ros2 node, and destroys/shutdown when ^C] |

**One place where the documentation helped me correct or avoid a mistake:**  
[Your answer]
