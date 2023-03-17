import win32api
import time

def check_mouse():
    savedpos = win32api.GetCursorPos()
    count = 0
    while(True):
        curpos = win32api.GetCursorPos()
        if savedpos != curpos:
            count = count +1
            savedpos = curpos
            print("Mouse Movement # ", count)
        time.sleep(0.05)
