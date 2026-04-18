import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys
import threading

class ChatNode(Node):
    def __init__(self, username):
        super().__init__('chat_node_' + username.lower())
        self.username = username
        
        # Publisher and Subscriber both use the same topic: /chat
        self.publisher_ = self.create_publisher(String, 'chat', 10)
        self.subscription = self.create_subscription(
            String,
            'chat',
            self.listener_callback,
            10)
        
        self.get_logger().info(f"Chat node started for [{self.username}]. Type your message and press Enter!")

    def listener_callback(self, msg):
        # We don't want to print our own messages back to us
        if not msg.data.startswith(f"[{self.username}]"):
            # Use '\r' and print to ensure the incoming message appears on a new line
            sys.stdout.write(f"\r{msg.data}\n> ")
            sys.stdout.flush()

    def send_message(self, text):
        msg = String()
        msg.data = f"[{self.username}]: {text}"
        self.publisher_.publish(msg)

def input_thread(node):
    """Thread to handle user input without blocking the ROS executor."""
    while rclpy.ok():
        user_input = input("> ")
        if user_input.lower() in ['exit', 'quit']:
            rclpy.shutdown()
            break
        node.send_message(user_input)

def main(args=None):
    rclpy.init(args=args)
    
    # Get username from command line argument
    if len(sys.argv) < 2:
        print("Usage: ros2 run <pkg_name> <node_name> <Username>")
        return

    username = sys.argv[1]
    chat_node = ChatNode(username)

    # Start the input thread
    thread = threading.Thread(target=input_thread, args=(chat_node,), daemon=True)
    thread.start()

    try:
        rclpy.spin(chat_node)
    except KeyboardInterrupt:
        pass
    finally:
        chat_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
