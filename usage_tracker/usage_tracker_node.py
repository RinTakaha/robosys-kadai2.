import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import datetime

class UsageTrackerNode(Node):
    def __init__(self):
        super().__init__('usage_tracker_node')

        # Publishers
        self.usage_time_publisher = self.create_publisher(String, '/usage_time', 10)

        # Timers and States
        self.start_time = None
        self.total_usage = datetime.timedelta()

        # Subscriptions
        self.create_subscription(String, '/start_time', self.start_time_callback, 10)
        self.create_subscription(String, '/stop_time', self.stop_time_callback, 10)

        self.get_logger().info('Usage Tracker Node has started.')

    def start_time_callback(self, msg):
        if self.start_time is None:
            self.start_time = datetime.datetime.now()
            self.get_logger().info(f"Start time recorded: {self.start_time}")
        else:
            self.get_logger().warn("Tracking is already running.")

    def stop_time_callback(self, msg):
        if self.start_time is not None:
            end_time = datetime.datetime.now()
            session_usage = end_time - self.start_time
            self.total_usage += session_usage

            # Publish usage time
            usage_msg = String()
            usage_msg.data = f"Session: {session_usage}, Total: {self.total_usage}"
            self.usage_time_publisher.publish(usage_msg)

            self.get_logger().info(f"Session ended. Duration: {session_usage}")
            self.start_time = None
        else:
            self.get_logger().warn("Tracking is not currently running.")

def main(args=None):
    rclpy.init(args=args)
    node = UsageTrackerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

