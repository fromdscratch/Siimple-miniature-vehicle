import network
import socket
import _thread
from machine import Pin
import time
f1=Pin(16,Pin.OUT)
f2=Pin(17,Pin.OUT)
f3=Pin(18,Pin.OUT)
f4=Pin(19,Pin.OUT)
trigger=Pin(22,Pin.OUT)
echo=Pin(21,Pin.IN)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("home","sun54321")
m=""
# #remote port
# UDP_IP = "192.168.134.148"
# UDP_PORT = 1234
 
# Wait for connect or fail
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    print('Wi-Fi Connected')
    ip=wlan.ifconfig()[0]
    print('Local IP: ', ip)
 
    
localIP  = wlan.ifconfig()[0]
localPort   = 1234
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print('Listening on Port - '+str(localPort))

def second_core_function():
    global m
    while True:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        m=str(message.decode())
        m=m.strip()
        print("Incoming Data : "+str(m)+" , From Address : "+str(address))
        message=input("enter a number: ")
     


_thread.start_new_thread(second_core_function, ())
 
while True:
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
       signaloff = time.ticks_us()
    while echo.value() == 1:
       signalon = time.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2 
    print("Total distance",distance,"cm")
    print("sensor")
    time.sleep(0.1)
    
    if distance<40:
        harish.high()
        sathyan.low()
        harish1.high()
        harish2.low()
    else:
        if str(m) =="front":  
            f1.high()
            f2.low()
            f3.high()
            f4.low()
        
        
        if str(m) == "back":  
            f1.low()
            f2.high()
            f3.low()
            f4.high()
             
            
        if str(m) == "left":   
            f1.high()
            f2.low()
            f3.low()
            f4.low()
    #       sleep(5)
             
        if str(m) == "right":  
            f1.low()
            f2.low()
            f3.high()
            f4.low()
    #       sleep(5)

        if str(m) == "stop":  
            f1.high()
            f2.high()
            f3.high()
            f4.high()
        
        
     
       
        

 

