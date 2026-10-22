
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SicaklikIzleyici(Node):
    def __init__(self):
        super().__init__('sicaklik_izleyici')

        # Sicaklik esigini ROS 2 parametresi olarak tanimla
        self.declare_parameter('sicaklik_esigi', 30.0)
        self.sicaklik_esigi = self.get_parameter(
            'sicaklik_esigi'
        ).value

        self.subscription = self.create_subscription(
            Float32,
            '/sicaklik',
            self.sicaklik_callback,
            10
        )

        self.get_logger().info(
            f'Sicaklik izleyici baslatildi. '
            f'Esik: {self.sicaklik_esigi} C'
        )

    def sicaklik_callback(self, msg):
        sicaklik = msg.data

        self.get_logger().info(
            f'Gelen sicaklik: {sicaklik:.1f} C'
        )

        if sicaklik > self.sicaklik_esigi:
            self.get_logger().warning(
                f'UYARI! Sicaklik {self.sicaklik_esigi} C '
                f'ustunde: {sicaklik:.1f} C'
            )


def main(args=None):
    rclpy.init(args=args)
    node = SicaklikIzleyici()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
