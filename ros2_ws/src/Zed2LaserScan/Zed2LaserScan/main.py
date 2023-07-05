import rclpy
from rclpy.node import Node
import pcl
import numpy as np
import ros_numpy
from sensor_msgs.msg import PointCloud2, LaserScan

class PointCloudToLaserScanNode(Node):
    def __init__(self):
        super().__init__('Zed2LaserScan')
        self.sub = self.create_subscription(PointCloud2, 'zed2/point_cloud/cloud_registered', self.callback, 10)
        self.pub = self.create_publisher(LaserScan, 'zed2/laser_scan', 10)

    def callback(self, msg):
        pc_array = ros_numpy.point_cloud2.pointcloud2_to_array(msg)
        
        # TODO: Get x and y values from point cloud
        # TODO: Discard points with z values outside of a certain range

        pass


def main(args=None):
    rclpy.init(args=args)
    node = PointCloudToLaserScanNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
