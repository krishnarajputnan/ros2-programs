import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        # Create a publisher for the /raw_signal topic
        self.publisher_ = self.create_publisher(Int32, 'raw_signal', 10)
        # Create a timer that runs every 1.0 seconds (1 Hz)
        self.timer = self.create_timer(1.0, self.timer_callback)
        # Start the counter at 2
        self.count = 2

    def timer_callback(self):
        msg = Int32()
        msg.data = self.count
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')
        # Add 2 for the next time it runs
        self.count += 2

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
