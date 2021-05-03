#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Empty
from kobuki_msgs.msg import Sound

class QrCodeReader:

    def __init__(self):
        rospy.init_node('qr_code_reader', anonymous=True)

        # First publisher
        self.pub_sound = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=10)
        #self.pub_stop_nav = rospy.Publisher('/stop_navigation', Empty, queue_size=10)
        #self.pub_start_nav = rospy.Publisher('/start_navigation', Empty, queue_size=10)

        self.msg_sound = Sound()
        self.msg_sound.value = 2
        
        # Then subscriber
        rospy.Subscriber('/qr_codes', String, self.callback)

    def callback(self, data):
        rospy.loginfo(data.data)
        qr_code = data.data
        if (qr_code == 'start'):
            self.msg_sound.value = 2
            self.pub_sound.publish(self.msg_sound)
            #self.pub_start_nav.publish()
        elif (qr_code == 'stop'):
            self.msg_sound.value = 6
            self.pub_sound.publish(self.msg_sound)
            #self.pub_stop_nav.publish()
        elif (qr_code == 'finish'):
            self.msg_sound.value = 2
            self.pub_sound.publish(self.msg_sound)
        elif (qr_code == 'drop_area'):
            self.msg_sound.value = 2
            self.pub_sound.publish(self.msg_sound)
        elif (qr_code == 'blue_block'):
            self.msg_sound.value = 2
            self.pub_sound.publish(self.msg_sound)
        elif (qr_code == 'red_block'):
            self.msg_sound.value = 2
            self.pub_sound.publish(self.msg_sound)

if __name__ == '__main__':
    try:
        q = QrCodeReader()
        rospy.spin() 
    except rospy.ROSInterruptException:
        pass