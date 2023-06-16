#!/usr/bin/env python3
import time
import serial
import sys, getopt



def main(argv):
   
   try: 
        recipient = ""
        message = ""
        phone = serial.Serial("/dev/ttyUSB2", 115200, timeout = 5) 
        opts, args = getopt.getopt(argv,"hr:m:",["recipient=","message="])
        for opt, arg in opts:
           if opt == '-h':
             print ('sendsms.py -r <recipient> -m <message>')
             sys.exit()
           elif opt in ("-r", "--recipient"):
             recipient = arg
           elif opt in ("-m", "--message"):
             message = arg
        print ('recipient is ', recipient)
        print ('message is ', message)
        time.sleep(0.5)
        phone.write(b'ATZ\r')
        time.sleep(0.5)
        phone.write(b'AT+CMGF=1\r')
        time.sleep(0.5)
        phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r') 
        time.sleep(0.5)
        phone.write(message.encode())
        time.sleep(0.5)
        phone.write(bytes([26]))
        time.sleep(0.5)
   finally: 
        phone.close()

if __name__ == "__main__":
   main(sys.argv[1:])