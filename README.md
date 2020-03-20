# Welcome to my tutorial on a quick creation of a bot for virutaly anything on a pc in python!

Tutorial by <b>Patrick Gray</b>.


This guide will teach you some python for the use of creating program to automate work without the ability to read and write process memory. this Program will match pixles by color and pattern. That bieng said your render is a 3d enviroment and we are scanning in a 2d manner this could cause some problems, and I will explain later a method to over come that.

okay so setting up the enviroment is key!

Download and install pycharm https://www.jetbrains.com/pycharm/


<b>import the folowing packages:pyautogui,time,randomint from the random package
  </b>


if you are unfamiliar with how to install modules in pycharm please check this out https://www.jetbrains.com/pycharm/guide/tips/install-and-import/



for documents on pyautogui please check out https://pyautogui.readthedocs.io

this document will explain what the functions are doing and the importance of the logic!
please see <b>Main.py</b>



Gathering custom .png files is simple take a screenshot of the current screen with the PrtSc button paste this in paint crop the area that make the item unique from the rest of the screen create a new paint file paste the cropped image. make sure to remove any whitespixles caused by paints easle you can do so by clicking the gray area arround it and dragging the bottom left box up and right as needed.


getting mouse coordinates can be done the same way in paint as you drag your mouse it will show the coordinates as if it where on screen the verry top left starting at 0,0 for info on screen resolution and how you can use the pyautogui with it check out:https://pyautogui.readthedocs.io/en/latest/mouse.html#the-screen-and-mouse-position.

#TODO
  create a virtual mouse so it can interact with the game while I do other things
