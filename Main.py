import pyautogui,time
from random import randint
#for setup you will need a folder named Pictures, inside of this you will need 4 png files named as followed
# sandstone.png
# sandstone1.png
# grind.png
# mine.png
# see readme on how to create your own

#lets allow the time for the program to sleep so we can minimise pycharm this will be usefull for testing
time.sleep(3)
#This tutorial we will make a bot for Runescape and avoid some  heuristic detection by adding randomness

# okay so for some prep work you need to get the exact camera angle because we are working with pixle detection in a 3d enviorment we need to basically take the "3d" out of the enviroment so all the pixels and colors will match our files
# this can be done by left clicking on the compass near the minimap and restricting the zoom in the settings, this will ensure the exact camera angle each time

# for this example we will create and autominer that mines sanstone and processess it into sand
def mine():
    sandstone = None # declaring a variable sandstone and set the value to none than search on screen 20 itterations for the file in Pictures/sandstone.png
    for i in range(1,20):
        sandstone = pyautogui.locateOnScreen('Pictures/sandstone.png',confidence=.95) # this will result in the output of bbox with grid coordinates that we can work with
    pyautogui.moveTo(sandstone, duration=1.2, tween=pyautogui.easeOutQuad)# okay so lets break this down pyautogui.moveTo this moves the mouse the tween allows different options this one starts the movement fast and slows down to be as humanly accurate as possible
    pyautogui.rightClick()
    mine = None
    for i in range(1,3):
        mine = pyautogui.locateOnScreen('Pictures/mine.png') # searches 3 itterations for mine.png or the bitmap we pointed it to
    pyautogui.moveTo(mine, duration=1.2)
    pyautogui.click()
    time.sleep(randint(10,12))# set the sleep time so the stamina bar only gets about half way down


def grind():
    sandstone1 = None
    for i in range(1,10):
        sandstone1 = pyautogui.locateOnScreen('Pictures/sandstone1.png', minSearchTime=1,confidence=.8) # the confidence argument is usefull if you bot is not clicking on anything try setting the confidence argument to say 0.65, 1 bieng a perfect match
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

# Okay so lets explain the logic below we create a never ending loop, each loop we search the last inventory slot to see if its filled or not 20 times
# if the last inventory slot has something in it it will execute the grind function if it does not it will execute the mine function several times until the last slot is filled usually 3-4 times
# in the grind function the sleep is not random as Runescape gives you the time it takes to craft all 26-27 pieces into sand
while True:
    for i in range(1,20):
        empytbag = pyautogui.locateOnScreen('Pictures/emptybag.png',confidence=.65,region=(1722,748, 200,450)) # the region argument states where on screen you want to look for the matching pixles. If coloration is an issue try using the grayscale=True argument
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
    # so the first attempt at writing this I tried a while statement for each function and it didnt work as smoothly
    # if you want to make this code look a little better you could create classes but this was intended for fast setup
