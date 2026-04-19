import rclpy
from rclpy.node import Node
import cv2
import numpy as np

class VisualLock(Node):
    def __init__(self):
        super().__init__('visual_lock')
        self.timer = self.create_timer(0.033, self.process_frame)
        self.current_state = "STARTING"
        
        # --- SIMULATOR VARIABLES ---
        self.sim_x = 320  # Start in the middle
        self.sim_dir = 10 # Speed of the ball

    def process_frame(self):
        # 1. GENERATE FAKE CAMERA FRAME (640x480 black screen)
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # Move the fake object
        self.sim_x += self.sim_dir
        
        # Make it bounce off-screen so we can test the "SEARCHING" state
        if self.sim_x > 800 or self.sim_x < -100:
            self.sim_dir *= -1
            
        # Draw a Blue circle (BGR format) if it is roughly on screen
        if -50 < self.sim_x < 700:
            cv2.circle(frame, (self.sim_x, 240), 40, (255, 0, 0), -1)

        # ---------------------------------------------------------
        # THE REST OF YOUR VISION LOGIC
        # ---------------------------------------------------------
        height, width, _ = frame.shape
        third_w = width // 3

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_blue = np.array([100, 150, 0])
        upper_blue = np.array([140, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        object_x = -1 
        
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest_contour) > 500:
                M = cv2.moments(largest_contour)
                if M["m00"] != 0:
                    object_x = int(M["m10"] / M["m00"])
                    cv2.circle(frame, (object_x, int(M["m01"] / M["m00"])), 5, (0, 255, 0), -1)

        # STATE MACHINE & FILTERS
        new_state = ""
        output_frame = frame

        if object_x == -1:
            new_state = "SEARCHING"
            output_frame = cv2.bitwise_not(frame) # Invert
            
        elif object_x < third_w:
            new_state = "ALIGNING LEFT"
            output_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Grayscale
            
        elif object_x > (2 * third_w):
            new_state = "ALIGNING RIGHT"
            output_frame = cv2.Canny(frame, 100, 200) # Edge Detect
            
        else:
            new_state = "LOCKED ON"
            output_frame = frame # Normal

        if new_state != self.current_state:
            self.get_logger().info(f"State: {new_state}")
            self.current_state = new_state

        cv2.imshow("Visual Lock (Simulated Target)", output_frame)
        cv2.waitKey(1)

    def destroy_node(self):
        cv2.destroyAllWindows()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = VisualLock()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
