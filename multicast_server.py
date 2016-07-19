
import serial
import socket
import struct
import sys

message = 'very important data'
multicast_group = ('224.3.29.71', 10000)

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

command = "MEASure:VOLTage:DC? (@101)\n" #Writes to SerialPort

def read_agilent():
	ser.write(command)	
	bytes = ser.readline()  #Reads from SerialPort
	return bytes

init_serial()

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(0.2)

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
while 1:
	message = read_agilent()
	# Send data to the multicast group
	print >>sys.stderr, 'sending "%s"' % message
	sent = sock.sendto(message, multicast_group)

	# Look for responses from all recipients
	while 1:
		print >>sys.stderr, 'waiting to receive'
		try:
			data, server = sock.recvfrom(16)
		except socket.timeout:
			print >>sys.stderr, 'timed out, no more responses'
			break
		else:
			print >>sys.stderr, 'received "%s" from %s' % (data, server)
#print >>sys.stderr, 'closing socket'
#sock.close()
