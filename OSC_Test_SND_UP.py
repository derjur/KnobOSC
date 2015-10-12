# OSC Knobber - derjur@gmail.com

# Load pyOSC 
# pyOSC is installed with pip
# Currently only works with Python2.7
import optparse
from OSC import *
from OSC import _readString, _readFloat, _readInt

# Build our client connection 
# This is the OSC endpoint we wish to send data to
clientobject = OSCClient()
clientobject.print_tracebacks = True

clientaddress = "127.0.0.1"
clientport = 50106

# Connect to the client object
clientobject.connect((clientaddress,clientport))
#print clientobject

# Build message data
msg = OSCMessage()
msg.setAddress("/dev/0/0/mon")
msg.append(0.4)

# Send the message data
print "Sending ", msg, " to ", clientaddress, " on port ", clientport

clientobject.send(msg)

# Clean up 
clientobject.close()


