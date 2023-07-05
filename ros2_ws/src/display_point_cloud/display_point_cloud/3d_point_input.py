import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import point_cloud2

class PointCloudDisplay(Node):
    def __init__(self):
        super().__init__('point_cloud_display')
        self.sub = self.create_subscription(PointCloud2, 'zed2/point_cloud/cloud_registered', self.cloud_callback, 10)
        self.sub.assert_future().add_done_callback(self.sub_callback)

    def sub_callback(self, future):
        self.get_logger().info('PointCloud2 Subscription Successful')

    def cloud_callback(self, cloud_msg):
        cloud_arr = np.asarray(list(point_cloud2.read_points(cloud_msg, field_names=("x", "y", "z"), skip_nans=True)))
        x = cloud_arr[:,0]
        y = cloud_arr[:,1]
        z = cloud_arr[:,2]
        color = np.zeros((cloud_arr.shape[0],3), dtype=np.uint8)
        color[:] = (255,0,0)

        cloud = np.zeros((cloud_arr.shape[0],6), dtype=np.float32)
        cloud[:,0] = x
        cloud[:,1] = y
        cloud[:,2] = z
        cloud[:,3:6] = color

        cloud = cloud.reshape(-1,3,6).astype(np.float32)
        cloud = cloud[np.any(cloud[..., :3] != 0, axis=(1,2))]

        cloud_img = cloud[...,3:].astype(np.uint8)

        cv2.imshow('3D Point Cloud', cloud_img)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = PointCloudDisplay()
    rclpy.spin(node)
    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
