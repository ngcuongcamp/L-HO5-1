import pyautogui
import time
import keyboard


print("start")
time.sleep(3)
print("start type")
data = "111111111111111111"

pyautogui.write(data)
keyboard.press_and_release("enter")
