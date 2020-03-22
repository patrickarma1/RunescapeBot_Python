import subprocess
try:
import pyautogui
except ImportError:
    subprocess.Popen(['pip install pyautogui']stdout=subprocess.PIPE,universal_newlines=True)
   print("\r""installing pyautogui",end='')
# displays x and y coordinates of mouse updating in console without multiple lines

def get_pos():
    pos = pyautogui.position()
    print("\r", pos, end="")
while True:
    get_pos()
