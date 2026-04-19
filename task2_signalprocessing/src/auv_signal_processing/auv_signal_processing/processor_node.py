import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class ProcessorNode(Node):
    def __init__(self):
        super().__init__('processor_node')
        # Subscribe to the /raw_signal topic
        self.subscription = self.create_subscription(Int32, 'raw_signal', self.listener_callback, 10)
        # Create a publisher for the /processed_signal topic
        self.publisher_ = self.create_publisher(Int32, 'processed_signal', 10)

    def listener_callback(self, msg):
        new_msg = Int32()
        # Multiply the incoming number by 5
        new_msg.data = msg.data * 5
        self.publisher_.publish(new_msg)
        self.get_logger().info(f'Received: {msg.data}, Published to next node: {new_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ProcessorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
