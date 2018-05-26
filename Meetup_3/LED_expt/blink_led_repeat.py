'''
Task : Program to blink the led 10 times
Author : Vigneshwer
Date : 13th July 16
Version : 1.0
'''

#loading modules
from gpiozero import LED, Button
from time import sleep

#led function
def blink_led(time):
	
	led = LED(4)
	print "LED IS ON !!"
	led.on()
	sleep(time)
	print "LED IS OFF !!"
	led.off()
	sleep(time)

#main function
if __name__ == "__main__":
	#Switch on and off time
	on_off_time = 2
	#Repeat blinks
	repeat_time = 5
	for i in xrange(repeat_time):
		print "Blink number :-" + str(i) + "\n"
		#call the blink function 
		blink_led(on_off_time)
	

