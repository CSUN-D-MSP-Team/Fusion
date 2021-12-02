import rospy
from std_msgs.msg import String
from smbus import SMBus
import time

from ultrasonic import Ultrasonic

# define the hello world publisher function to call in ros terminal
def hello_world_pub():
    rospy.init_node("hello_world_pub_node")
    pub  = rospy.Publisher("hello_world", String, queue_size=10)
    
    sonar = Ultrasonic() # Default Constructor
    range = 0
    while(1):
        range = sonar.take_range_reading() # Returns int
        while not rospy.is_shutdown():
            pub.publish('Range: {} cm'.format(range))
            pub.publish('--------------------------')

#how to create main loop and run the publisher function
if __name__ == "__main__":
    try:
        hello_world_pub()

    except rospy.ROSInterruptException:
        pass
