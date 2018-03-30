import rospy
from std_msgs.msg import Int32
from challenge.msg import CustomMessage


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "\nReceived {} from node1"
                  .format(data.data))
    new_number = get_number()
    pub.publish(data.data, new_number)


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
    while not rospy.is_shutdown():
        sub
        rospy.Rate(1).sleep()


if __name__ == "__main__":
    pub = rospy.Publisher('node2', CustomMessage, queue_size=10)
    sub = rospy.Subscriber('node1', Int32, callback)
    rospy.init_node('node2')
    run_node()
