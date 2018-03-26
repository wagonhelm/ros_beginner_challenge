import rospy
from std_msgs.msg import String


def talker():
    count = 0
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1)  # 10 Hz
    while not rospy.is_shutdown():
        hello_str = "hellow world {}".format(rospy.get_time())
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        count += 1
        if count == 55:
            rospy.signal_shutdown('whatever')
            rospy.on_shutdown(h)


def h():
    print('foobar')


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
