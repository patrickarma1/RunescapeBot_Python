import subprocess
print("subprocess successfully imported")
try:
    import pyautogui
    print("pyauogui imported")
except ImportError:
    subprocess.call('pip install pyautogui')
    print("\r""installing pyautogui",end='')
try:
    from keyboard import is_pressed
    print("keyboard imported")
except ImportError:
    subprocess.call('pip install keyboard')
    print("\r""installing keyboard",end='')
# displays x and y coordinates of mouse updating in console without multiple lines

def get_pos():
    pos = pyautogui.position()
    print("\r", pos, end="")

q = (keyboard.is_pressed("q"))
While q is False:
     print("[+] Detected breakpoint ..... Exiting.")
      get_pos()
      if q is True:
        break
