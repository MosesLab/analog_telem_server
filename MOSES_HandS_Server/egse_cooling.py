#python egse_cooling.py

'''
Purpose:
Roy and I want to create a code in Python that allows us to communicate with an Aglient 34970a via RS-232 connection. 
Using SCPI commands, we will be able to configure the agilent to measure whatever we need to record, and take those measurements.
This code will be used to emulate a LabVIEW virtual machine without having the trouble of actually using LabVIEW. We will implement this code 
in our EGSE so we can communicate with the onboard electronics prior to flight.
'''

'''
Modification Sequence:
	13-Jul-2016:  N. Bonham -Created code
'''


#Establish communication using serial port
import serial

#Global Variables
ser = 0

#Function to Initialize the Serial Port
def init_serial():
	global ser
	ser = serial.Serial()
	ser.baudrate = 9600   #Determines baud rate (rate at which information is transferred in a communication channel). 9600 bits/second.

	ser.port = '/dev/ttyUSB0' 

	#Sets the TimeOut in seconds, so that SerialPort doesn't miscommunicate
	ser.timeout = 10
	ser.open()			#Opens SerialPort

	# print if port is open or closed
	if ser.isOpen():
		print 'Open: ' + ser.portstr
#End of Initialize Function


#Call the Serial Initialize Function, Main Program Starts from
init_serial()

#Write SCPI Commands here. This is how you can communicate with the Agilent.

#command = "*RST\n"
command = "MEASure:VOLTage:DC? (@101)\n"   #Writes to SerialPort



	 


#Attempt to create 2d array to fill with data points from Agilent








