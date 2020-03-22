import subprocess
print("subprocess successfully imported")
try:
    import pyautogui
    print("pyauogui imported")
except ImportError:
    subprocess.call('pip install pyautogui')
    print("\r""installing pyautogui",end='')
# displays x and y coordinates of mouse updating in console without multiple lines

def get_pos():
    pos = pyautogui.position()
    print("\r", pos, end="")
while True:
    get_pos()
