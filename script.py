import webbrowser
import time
import pyautogui
url=input("Enter Facebook Url ? ")
webbrowser.open(url)
time.sleep(7)
pyautogui.hotkey('ctrl','f')
pyautogui.typewrite("what's on your mind?")
pyautogui.press('enter')
pyautogui.press('escape')
pyautogui.press('enter')
time.sleep(4)
pyautogui.typewrite("Python Script")
pyautogui.click(650,585)
 
