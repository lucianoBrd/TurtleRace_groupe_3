#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from kobuki_msgs.msg import ButtonEvent

class Gripper:

    def __init__(self):
        rospy.init_node('gripper', anonymous=True)

        # First publisher
        self.pub_gripper = rospy.Publisher('/gripper_joint/command', Float64, queue_size=10)

        self.msg_gripper = Float64()
        self.msg_gripper.data = 1.0
        self.pub_gripper.publish(self.msg_gripper)
        
        # Then subscriber
        rospy.Subscriber('/mobile_base/events/button', ButtonEvent, self.callback)
        
    def callback(self, data):
        
        btn = data.state
        if (btn == 1):
            rospy.loginfo(data.state)
            self.msg_gripper.data = 0.6
            self.pub_gripper.publish(self.msg_gripper)
        
if __name__ == '__main__':
    try:
        g = Gripper()
        rospy.spin() 
    except rospy.ROSInterruptException:
        pass