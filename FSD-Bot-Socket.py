"""
Software Name: FSD-Bot-Socket
Version: 1.0.0
Author: XLiao
Copyright (c) 2023 by XLiao ❤
License: This software is licensed under the MIT License.
"""
import socket
import time

class FsdSocketClient:
    def __init__(self, hostName, port, userCall, userName, userPwd):
        # Initialize an instance of the FsdSocketClient class
        self.hostName = hostName  # FSD server hostname
        self.port = port  # FSD server port
        self.userCall = userCall  # User call name
        self.userName = userName  # User name
        self.userPwd = userPwd  # User password

    def FsdBot(self):
        print("Software Name: FSD-Bot-Socket")
        print("Version: 1.0.0")
        print("Author: XLiao")
        print("License: This software is licensed under the MIT License.")
        print("If customization is needed, please contact XLiao(QQ: 2456666787)")
        # Define the FsdBot method to handle communication with the FSD server
        botName = self.userName  # Get user name
        botUser = self.userCall  # Get user call name
        botPwd = self.userPwd  # Get user password
        # Create a socket and connect to the FSD server
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_client.connect((self.hostName, self.port))
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"{timestamp} Successfully established a connection with the server!")
        
        # Create write and read file objects for the socket
        socket_out = socket_client.makefile('w')
        socket_in = socket_client.makefile('r')

        # Send login message
        socket_out.write(f"#AA{botName}:SERVER:{botName}:{botUser}:{botPwd}:12:9:1:0:30.872780:104.391390:0\n%{botName}:21600:12:20:2:30.872780:104.391390:0\n$SXC{botName}:SERVER:ATC:{botName}\n$SXC{botName}:SERVER:CAPS\n$SXC{botName}:SERVER:127.0.0.1\n")
        socket_out.flush()

        # Read login response
        line = socket_in.readline()
        split = line.strip().split(":")

        if split[0] == "#TMserver":
            # If the server response starts with "#TMserver", login is successful

            while True:
                # Enter an infinite loop to continuously receive messages from the server
                line = socket_in.readline()
                if line and line != "":

                    if line.startswith("#AA"):
                        # If the message starts with "#AA", an ATC is online
                        messageSplit = line.strip().split(":")
                        seat_name = messageSplit[0][3:]  # Get the Seat name
                        atc_name = messageSplit[3]  # Get the login username

                        # Write the functionality needed for ATC online here

                    if line.startswith("#DA"):
                        # If the message starts with "#DA", an ATC is offline
                        messageSplit = line.strip().split(":")
                        seat_name = messageSplit[0][3:]  # Get the Seat name
                        atc_name = messageSplit[1]  # Get the login username

                        # Write the functionality needed for ATC offline here

                    if line.startswith("#AP"):
                        # If the message starts with "#AP", a pilot is online
                        messageSplit = line.strip().split(":")
                        flight_number = messageSplit[0][3:]  # Get the flight number
                        pilot_name = messageSplit[2]  # Get the login username

                        # Write the functionality needed for user online here

                    if line.startswith("#DP"):
                        # If the message starts with "#DP", a pilot is offline
                        messageSplit = line.strip().split(":")
                        flight_number = messageSplit[0][3:]  # Get the flight number
                        pilot_name = messageSplit[1]  # Get the login username

                        # Write the functionality needed for user offline here

        else:
            # If the server response doesn't start with "#TMserver", login failed
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"{timestamp} Login failed! Server response data: {split[-1]}")

# User settings, recommended level is 12
hostName = '' # Host name or IP
port = 6809
userCall = ''  # User name
userName = ''  # Position name
userPwd = ''  # User password

# Create an instance of FsdSocketClient and call the FsdBot method
fsdSocketClient = FsdSocketClient(hostName, port, userCall, userName, userPwd)
fsdSocketClient.FsdBot()
