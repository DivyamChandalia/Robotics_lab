import rclpy
import cv2
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class Capture(Node):
    def __init__(self):
        super().__init__('video_subscriber')
        self.subscriber = self.create_subscription(Image, '/camera1/image_raw', self.process_data, 10)
        self.out = cv2.VideoWriter('/home/divyam/divyam_ws/output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (512, 512))
        self.bridge = CvBridge()

    def process_data(self, data):
        frame = self.bridge.imgmsg_to_cv2(data)
        self.out.write(frame)
        self.img = cv2.imwrite('/home/divyam/divyam_ws/shot.png', frame)
        cv2.imshow("output", frame)
        cv2.waitKey()
        cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    node = Capture()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()