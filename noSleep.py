import pyautogui
import time


#move stop and then move again to coordinates
while(True):
    pyautogui.press('volumedown')
    time.sleep(5)
    pyautogui.press('volumeup')
    time.sleep(5)
