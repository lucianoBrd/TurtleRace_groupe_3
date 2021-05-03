#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from kobuki_msgs.msg import Sound

class QrCodeReader:

    def __init__(self):
        rospy.init_node('qr_code_reader', anonymous=True)

        # First publisher
        self.pub_sound = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=10)
        #self.pub_stop_nav = rospy.Publisher('/stop_navigation', Sound, queue_size=10)
        #self.pub_start_nav = rospy.Publisher('/start_navigation', Led, queue_size=10)

        self.msg_sound = Sound()
        self.msg_sound.value = 2
        
        # Then subscriber
        rospy.Subscriber('/qr_codes', Float32, self.callback)
        

    def callback(self, data):
        rospy.loginfo(data.data)
        if (data == 'start'):
            self.msg_sound.value = 2
            self.pub_sound.publish(self.msg_sound)
        else if (data == stop):
            self.msg_sound.value = 6
            self.pub_sound.publish(self.msg_sound)


if __name__ == '__main__':
    try:
        q = QrCodeReader()
        rospy.spin() 
    except rospy.ROSInterruptException:
        pass