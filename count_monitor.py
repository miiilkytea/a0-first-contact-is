#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class CountSubscriber(Node):

    def __init__(self):
        super().__init__('count_monitor')
        self.subscription = self.create_subscription(
            Int32,
            '/lab0/count',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('System Ready: I heard "%d"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    count_monitor = CountSubscriber()

    rclpy.spin(count_monitor)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    count_monitor.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
