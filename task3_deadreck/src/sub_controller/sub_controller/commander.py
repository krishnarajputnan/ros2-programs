import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Commander(Node):
    def __init__(self):
        super().__init__('commander')
        self.publisher_ = self.create_publisher(String, '/cmd', 10)
        self.get_logger().info("Commander Node Started. Enter: forward, backward, turn left, turn right")
        self.timer = self.create_timer(0.1, self.get_input)

    def get_input(self):
        cmd = input("Enter Command: ").strip().lower()
        msg = String()
        msg.data = cmd
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = Commander()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
