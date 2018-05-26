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
def blink_led():
	led = LED(4)
	print "LED IS ON !!"
	led.on()
	sleep(5)
	print "LED IS OFF !!"
	led.off()

#main function
if __name__ == "__main__":
	
	#call the blink function 
	blink_led()
	

