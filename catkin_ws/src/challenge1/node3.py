import rospy
from std_msgs.msg import Int32

pub = rospy.Publisher('node2', Int32, queue_size=10)
rospy.init_node('node2')

while not rospy.is_shutdown():
    pub.publish(14)
    rospy.Rate(10).sleep()