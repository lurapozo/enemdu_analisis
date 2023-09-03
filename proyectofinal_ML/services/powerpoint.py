import pyautogui as py
import os
import time

def init_presentetation(num_slides):
    os.startfile("presentation.pptx")
    time.sleep(3)
    py.press("f5")
    time.sleep(2)
    for _ in range(num_slides):
        """
        INSERTAR TTS
        """
        time.sleep(2)
        change_slide()
    time.sleep(1)
    py.press("esc")

def change_slide():
    py.press("right")