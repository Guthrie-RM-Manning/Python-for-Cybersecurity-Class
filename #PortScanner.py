#PortScanner.py
# -----READ ME-----
# This is a port scanner program built using python's socket module
# the user inputs a IP & Port
#It then calls the portScanner module and checks to see if the port specified is open

#------RESOURCES USED------
#  https://realpython.com/python-sockets/
#  https://docs.python.org/3/library/socket.html 

#begin PortScanner.py

import socket #this module is used to create connections

#define a function named portScanner to house the port scanner program
def portScanner(targetIP, targetPort):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET = IPv4, SOCK_STREAM = TCP
    try:
        #I did it this way to ensure that I don't have to close the socket at the end each time manually
        with sock as s: #used a website I found and this was kind of how they wrote it, so I copied and played around with it
            s.settimeout(2) # sets the timeout (adjust the number in () to increase or decrease the time - in seconds)
            connection = s.connect_ex((targetIP , targetPort)) #creates a connection with the IP:Port combo that the user will supply
            if connection == 0: #connections that return a 0 are open - anything else is closed or error
               #inform whether the socket is open or closed
                print(f'The port {targetPort} is open')
            else: 
                print(f'The port {targetPort} is closed')
    #handle other errors like the connection timing out and any error other exception it returns
    except socket.timeout:
        print('The connection timed out')
    except Exception as e: 
        print(f'Oops! An error {e} has occured')

#get user unput
targetIP = input('please enter your Target IP: ')
targetPort = int(input('please enter your target port: '))
#calling port scanner function
portScanner(targetIP, targetPort)