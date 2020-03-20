import pyautogui,time
from random import randint

time.sleep(3)
def mine():
    sandstone = None
    for i in range(1,20):
        sandstone = pyautogui.locateOnScreen('Pictures/sandstone.png',confidence=.95)
    pyautogui.moveTo(sandstone, duration=1.2, tween=pyautogui.easeOutQuad)
    pyautogui.rightClick()
    mine = None
    for i in range(1,3):
        mine = pyautogui.locateOnScreen('Pictures/mine.png')
    pyautogui.moveTo(mine, duration=1.2)
    pyautogui.click()
    time.sleep(randint(10,12))


def grind():
    sandstone1 = None
    for i in range(1,10):
        sandstone1 = pyautogui.locateOnScreen('Pictures/sandstone1.png', minSearchTime=1,confidence=.8)
    pyautogui.moveTo(sandstone1, duration=1.2, tween=pyautogui.easeOutQuad)
    pyautogui.rightClick()
    time.sleep(randint(1, 3))
    for i in range (1,3):
        grind = pyautogui.locateOnScreen('Pictures/grind.png')
    pyautogui.moveTo(grind, duration=1.2, tween=pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(randint(2, 3))
    pyautogui.press('space')
    time.sleep(38)


while True:
    for i in range(1,20):
        empytbag = pyautogui.locateOnScreen('Pictures/emptybag.png',confidence=.65,region=(1722,748, 200,450))
    if empytbag is not None:
        print("mining")
        mine()
        empytbag == None
        pass
    for i in range(1, 20):
        empytbag = pyautogui.locateOnScreen('Pictures/emptybag.png', confidence=.65,region=(1722, 748, 200, 450))

    if empytbag is None:
        print("grinding")
        grind()
        empytbag == 1
        pass
