import rospy
from challenge.msg import CustomMessage
from std_msgs.msg import Int32


def callback(data):
    rospy.loginfo(rospy.get_caller_id())
    print("{} + {} = {}"
          .format(data.number_1, data.number_2, data.number_1+data.number_2))
    pub.publish(data.number_1+data.number_2)


def get_number():
    while True:
        try:
            number = int(input("Enter a number between 1-1000: "))
            assert number in range(1, 1001), "Seriously?"
        except Exception as e:
            print(e)
        else:
            break
    return number


def run_node():
    number = get_number()
    pub.publish(number)
    while not rospy.is_shutdown():
        sub
        rospy.Rate(1).sleep()


if __name__ == "__main__":
    pub = rospy.Publisher('node1', Int32, queue_size=10)
    sub = rospy.Subscriber('node2', CustomMessage, callback)
    rospy.init_node('node1')
    run_node()
