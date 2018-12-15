#this is a python program to create an interface to interact with the arduino and. It is an IOT based program

import serial #this is to help connect to the device
import urllib #this is to help connect to the website
import time  #this is to help control the time interval in which a request is sent to the website
import json  #this is to help deserialize the data received from the website

address = raw_input('input the address to do the switching from')
print('please check the arduino sketch for the com port that you connect the arduino to')
comport = raw_input('input the comport of the device connected to the serial port that you wish to control')
baud = int(raw_input('input the baud rate of the device connected to serial port that you wish to control'))
arduino = serial.Serial(comport, baud)

def LED(state):
    """this is the arduino function that controls how the LED bulb with respect to what the webserver says"""
    if state == True:
        arduino.write(b'1')
        print('the arduino is in the ON state')
        return True
    else:
        arduino.write(b'0')
        print('the arduino is in the OFF state')
        return False

init_state = False
while True:
    url = urllib.urlopen(address) #this is where the opening of the url takes place
    try:
        state = json.loads(url.read())['state'] #this gets the wanted state of the device according to users want in the website
    except Exception as e:
        print('check the web address or your network connection it seems there seems to be a problem, ', e)
        state = init_state
    if not init_state == state: #this is to stop unneccessary calling of the arduino writing function
        LED(state)
    init_state = state
    time.sleep(1) #this is to control the interval of time that it takes for our application to make a given request

