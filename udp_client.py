import sys
import socket

TARGET_HOST = "www.google.com"
TARGET_PORT = 80

class Test:
    def __init__(self):
    #   self.test()
        create_client()
        self.connect()
        self.send_data()
       # self.recive_data()
        
    def create_client(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    
    def connect(self):
        self.client.connect((TARGET_HOST, TARGET_PORT))
        print("connected")
        
    def send_data(self):
        self.client.sendto("ABBACCCC", (TARGET_HOST, TARGET_PORT))
        print("about to send something... ")
        
    def recive_data(self):
        self.response = self.client.recvfrom(4096)
        print(self.response)
        
                         
                            
if __name__ == "__main__":
    Test()
