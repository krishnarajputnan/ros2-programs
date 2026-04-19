import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sub_interfaces.msg import BotPose

class Navigator(Node):
    def __init__(self):
        super().__init__('navigator')
        self.subscription = self.create_subscription(String, '/cmd', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(BotPose, '/bot_pose', 10)
        
        # Initial State
        self.x = 0.0
        self.y = 0.0
        self.facing = "North"
        
        # State Machine Logic
        self.directions = ["North", "East", "South", "West"]

    def listener_callback(self, msg):
        command = msg.data
        idx = self.directions.index(self.facing)

        if command == "turn right":
            self.facing = self.directions[(idx + 1) % 4]
        elif command == "turn left":
            self.facing = self.directions[(idx - 1) % 4]
        elif command == "forward" or command == "backward":
            move = 1.0 if command == "forward" else -1.0
            if self.facing == "North": self.y += move
            elif self.facing == "South": self.y -= move
            elif self.facing == "East": self.x += move
            elif self.facing == "West": self.x -= move

        self.publish_state()

    def publish_state(self):
        msg = BotPose()
        msg.x = self.x
        msg.y = self.y
        msg.facing_direction = self.facing
        self.publisher_.publish(msg)
        self.get_logger().info(f"Sub at ({self.x}, {self.y}) facing {self.facing}")

def main():
    rclpy.init()
    node = Navigator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
