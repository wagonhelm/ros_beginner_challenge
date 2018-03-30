import rospy
from std_msgs.msg import Int32

class Node2():
    
    
    def __init__(self):
        
        self.pub = rospy.Publisher('node2', Int32, queue_size=10)
        self.sub = rospy.Subscriber('node1', Int32, self.callback)
        rospy.init_node('node2')


    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "\nReceived {} from node1" \
                                               .format(data.data))
        print("Enter a number to add to {} and send back to node2".format(data.data))
        data.data += self.get_number()
        self.pub.publish(data.data)


    def get_number(self):
        while True:
            try:
                number = int(input("Enter a number between 1-1000: "))
                assert number in range(1, 1001), "Seriously?"
            except Exception as e:
                print(e)
            else:
                break
        return number


    def run_node(self):
       while not rospy.is_shutdown():
           self.sub
           rospy.Rate(1).sleep()
           
        
if __name__ == "__main__":
    node2 = Node2()
    node2.run_node()