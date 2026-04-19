import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class OutputNode(Node):
    def __init__(self):
        super().__init__('output_node')
        # Subscribe to the /processed_signal topic
        self.subscription = self.create_subscription(Int32, 'processed_signal', self.listener_callback, 10)

    def listener_callback(self, msg):
        # Add 10 to the incoming number
        final_result = msg.data + 10
        # Print the final result to the terminal
        self.get_logger().info(f'Final Result: {final_result}')

def main(args=None):
    rclpy.init(args=args)
    node = OutputNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()


