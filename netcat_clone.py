import sys
import socket
import getopt
import threading
import subprocess

#define some global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_des = ""
port = 0



def usage():
    print("")
    print("")
