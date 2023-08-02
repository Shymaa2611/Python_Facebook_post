import webbrowser
import time
import pyautogui
import random
import string
#===================== Create Account On PythonanyWhere=======================#
url='https://www.pythonanywhere.com/registration/register/beginner/'
url2='https://www.pythonanywhere.com/login/'
webbrowser.open(url)
time.sleep(5)
def generate_username():
    prefix = "pythonScript"
    suffix = ''.join(random.choices(string.digits, k=3))
    return prefix + suffix
username=generate_username()
def create_username(username):
    pyautogui.hotkey('ctrl','f')
    pyautogui.typewrite("username") 
    pyautogui.press('enter')
    pyautogui.press('escape')
    pyautogui.press('enter')
    pyautogui.click(400,250)
    pyautogui.typewrite(username)
create_username("pythonScript")
time.sleep(2)
pyautogui.hotkey('ctrl','f')
pyautogui.typewrite("Email")
pyautogui.press('enter')
pyautogui.press('escape')
pyautogui.press('enter')
pyautogui.click(400,300)
pyautogui.typewrite("PythonScript@gmail.com")
time.sleep(2)
pyautogui.hotkey('ctrl','f')
pyautogui.typewrite("Password")
pyautogui.press('enter')
pyautogui.press('escape')
pyautogui.press('enter')
pyautogui.click(400,350)
pyautogui.typewrite("PythonScript2345")
time.sleep(2)
pyautogui.hotkey('ctrl','f')
pyautogui.typewrite("Password(again)")
pyautogui.press('enter')
pyautogui.press('escape')
pyautogui.press('enter')
pyautogui.click(400,400)
pyautogui.typewrite("PythonScript2345")
time.sleep(2)
pyautogui.click(400,455)
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(500,450)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('ctrl','f')
text=pyautogui.typewrite("This username is already taken. Please choose another.")
if text is not None:
    print("GOOD")
else:
    username=generate_username()
    create_username(username)
    time.sleep(2)
    pyautogui.click(400,455)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(500,450)
    pyautogui.press('enter')
    time.sleep(2)


""" if text is not None:
    print("GOOD")
else:
    
    webbrowser.open(url2)
    time.sleep(10)
    create_username("pythonScript")
    time.sleep(2)
    pyautogui.hotkey('ctrl','f')    
    pyautogui.typewrite("Password")
    pyautogui.press('enter')
    pyautogui.press('escape')
    pyautogui.press('enter')
    pyautogui.click(400,400)
    pyautogui.typewrite("PythonScript2345")
    time.sleep(5)
    pyautogui.click(500,450)
    pyautogui.press('enter')
    time.sleep(2)
 """

