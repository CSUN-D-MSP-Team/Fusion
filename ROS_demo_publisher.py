import rospy
from std_msgs.msg import String

# define the hello world publisher function to call in ros terminal
def hello_world_pub():
	rospy.init_node("hello_world_pub_node")
	pub  = rospy.Publisher("hello_world", String, queue_size=10)

	# while loop to send message repeated
	i = 0
	while not rospy.is_shutdown():
		pub.publish("hello world" + str(i))
		i += 1
	
#how to create main loop and run the publisher function
if __name__ == "__main__":
	try:
		hello_world_pub()

	except rospy.ROSInterruptException:
		pass
