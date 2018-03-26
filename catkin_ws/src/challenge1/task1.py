import rospy
from std_msgs.msg import Int32


def talker():
    pub = rospy.Publisher('chatter', Int32, queue_size=10)
    rospy.init_node('sender')
    add = 0
    while not rospy.is_shutdown():
        while True:
            try:
                number = int(input("Enter a number between 1-1000: "))
                assert number in range(1, 1001), "Seriously..."
            except Exception as e:
                print(e)
            else:
                break
        added_number = add + number
        # rospy.loginfo(added_number)
        pub.publish(added_number)
        rospy.Rate(1).sleep()


if __name__ == "__main__":
    talker()
