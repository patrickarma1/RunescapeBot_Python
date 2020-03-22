import subprocess
try:
import pyautogui
except ImportError:
    
# displays x and y coordinates of mouse updating in console without multiple lines

def get_pos():
    pos = pyautogui.position()
    print("\r", pos, end="")
while True:
    get_pos()
