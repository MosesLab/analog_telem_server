# Impromptu library for taking voltage measurements with Agilent 34970A
import serial



#Function to Initialize the Serial Port
def init_serial():
    ser = serial.Serial()
    ser.baudrate = 9600   #Determines baud rate (rate at which information is transferred in a communication channel). 9600 bits/second.

    ser.port = '/dev/ttyUSB1'

    #Sets the TimeOut in seconds, so that SerialPort doesn't miscommunicate
    ser.timeout = None
    ser.open()			#Opens SerialPort

    # print if port is open or closed
    if ser.isOpen():
        print('Open: ' + ser.portstr)

    return ser


# Reads one measurement from A/D
def measure(ser, min_chan, max_chan):

    # Commands the agilent to read voltage on specified number of ports
    command = bytes("MEASure:VOLTage:DC? (@" + str(min_chan) + ":" + str(max_chan) + ")\n", 'utf-8')

    ser.write(command)
    return ser.readline().decode('utf-8')[:-2]  #Reads from SerialPort

def cleanup_serial(ser):

    ser.close()


