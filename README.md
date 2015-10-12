## Touch OSC Scripts for arbitrary value massaging

### Install
Python2.7 was used for development, and I believe it to be the only version that supports pyOSC.
Once python2.7 is installed, you can use ```pip install pyosc``` to install.  

In Windows, there will be a pythonw.exe in your python install directory.  This can be used to call scripts without opening a window.
I have not tried this on OSX/Linux yet, but I don't think you need to do anything to have this run in the background.  

The idea behind this project is to have an assignable script that can be triggered by hardware or software, to send OSC messages.
In my case, I bought a Griffin Powermate, and I'm assigning clockwise rotation to SND_UP and counter-clockwise to SND_DN.  Effectively granting me a huge master volume knob for my MOTU 828.  

### Notes
MOTU 828 CueMix Monitor Control:
/dev/0/0/mon  




*TODO*
 - Need to query/read the current value of the device.
 - Ensure that script cleans up (possible race condition is leaving open ended python processes)