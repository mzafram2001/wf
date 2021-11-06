from pyautogui import *
import pyautogui
import cv2
import pytesseract
import time
import keyboard
import random
import win32api, win32con
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

i = 1
ready = 0

while keyboard.is_pressed('q') == False:
    # Detectar campana
    if pyautogui.locateOnScreen('bell.png', region=(0,0,1366,738), grayscale=True, confidence=0.8) != None:
            print("BELL")
            click(497,53)
            time.sleep(0.5)
            i += 1
            
    # Click botón aceptar
    if pyautogui.locateOnScreen('accept.png', region=(0,0,1366,738), grayscale=True, confidence=0.8) != None:
            print("ACCEPT")
            click(752,621)
            time.sleep(0.5)
            i += 1

    # Click listo
    if (pyautogui.locateOnScreen('ready.png', region=(0,0,1366,738), grayscale=True, confidence=0.8) != None or pyautogui.locateOnScreen('readyEvent.png', region=(0,0,1366,738), grayscale=True, confidence=0.8) != None) and ready == 0:
            print("READY")
            click(666,544)
            time.sleep(0.5)
            i += 1
            ready = 1
            
    # Click siguiente x3
    if pyautogui.locateOnScreen('next.png', region=(0,0,1366,738), grayscale=True, confidence=0.8) != None:
            print("NEXT")
            click(670,684)
            time.sleep(0.5)
            i += 1

    # Abandonar sala
    if pyautogui.locateOnScreen('back.png', region=(0,0,1366,738), grayscale=True, confidence=0.8) != None:
            print("BACK")
            click(630,684)
            time.sleep(0.5)
            i += 1
            ready = 0
            
    # Ok
    if pyautogui.locateOnScreen('ok.png', region=(0,0,1366,738), grayscale=True, confidence=0.8) != None:
            print("OK")
            click(676,481)
            time.sleep(0.5)
            i += 1
            
    # Cada 5 LOGs, limpiamos
    if i == 10:
        os.system('cls')
