from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    try:
        pyautogui.click(x=x,y=y,button='left')
        time.sleep(0.01)
        print("Press")
    except Exception as e:
        print("Failed:" + str(e))

def erkundenSuchen():
    while keyboard.is_pressed('q') == False:
        hilfeSuchen('5.jpg', 0.7)
        erkennung('1.jpg', 0.7)
        erkennung('2.jpg', 0.6)
        time.sleep(0.05)

def erkennung(pic, confidence):
        if pyautogui.locateOnScreen(pic, confidence= confidence) != None:
            location = pyautogui.locateOnScreen(pic, confidence= confidence)
            print(location)
            if location != None:
                click(location.left + 40, location.top + 90)
                time.sleep(1)
                click(location.left + 180, location.top + 230)
                time.sleep(1)
                spaeherverwaltung()
        else:
            print(f"Ich sehe kein :{pic}")
            
def hilfeSuchen(pic, confidence):
    if pyautogui.locateOnScreen(pic, confidence=confidence) != None:
        location = pyautogui.locateOnScreen(pic, confidence= confidence)
        time.sleep(0.7)
        click(location.left + 20, location.top + 40)
        print('hilfe !!')
    else:
        print('keiner braucht hilfe')

        
def spaeherverwaltung():
    if pyautogui.locateOnScreen('3.jpg', confidence= 0.9) != None:
        location = pyautogui.locateOnScreen('3.jpg', confidence= 0.9)
        click(location.left, location.top)
    time.sleep(2)
    if pyautogui.locateOnScreen('3.jpg', confidence= 0.9) != None:
        location = pyautogui.locateOnScreen('3.jpg', confidence= 0.9)
        click(location.left, location.top)
    time.sleep(1)
    if pyautogui.locateOnScreen('4.jpg', confidence= 0.9) != None:
        location = pyautogui.locateOnScreen('4.jpg', confidence= 0.9)
        click(location.left, location.top)
    time.sleep(0.5)
    pyautogui.press('space')
    time.sleep(0.7)
    

erkundenSuchen()