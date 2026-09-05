#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('status_monitor')
        self.subscription = self.create_subscription(
            String,
            '/lab0/status',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('System Ready: I heard "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    status_publisher = MinimalSubscriber()

    rclpy.spin(status_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    status_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
