import rospy
from std_msgs.msg import Int32


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "\nYou entered {}".format(data.data))
    while True:
            try:
                number = int(input("Enter a number between 1-1000 to add: "))
                assert number in range(1, 1001), "Seriously..."
            except Exception as e:
                print(e)
            else:
                break
    print("{} + {} = {}".format(data.data, number, data.data+number))


def listener():
    rospy.init_node("listener")
    rospy.Subscriber("chatter", Int32, callback)
    rospy.spin()


if __name__ == "__main__":
    listener()
