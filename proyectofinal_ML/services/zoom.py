import pyautogui as py
import subprocess

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "C:\selenium_drivers\chromedriver")
driver.maximize_window()

def connect_zoom(meet_code, password):
    driver.get(f"https://zoom.us/j/{meet_code}?pwd={password}")
    sleep(2)
    py.press("left")
    sleep(1)
    py.press("enter")
    sleep(2)
    driver.close()
    # Si se tiene abierto el client de zoom se demora en promedio 10s y si no la tiene abierto en promedio 16-20s
    print("Abriendo y Cargando Reunion de Zoom")
    sleep(16)
    print("En Zoom")
    sleep(1)
    py.getWindowsWithTitle("Zoom Meeting")[0].maximize()
    # share_screen()
    # sleep(1)
    # write_chat()
    # sleep(1)
    # disconnect_zoom()
    
def disconnect_zoom():
    print("Cerrando")
    py.hotkey('alt', 'q')
    py.press('enter')

def share_screen():
    py.hotkey('alt', 'S')
    sleep(1)
    py.press('enter')

def stop_share_screen():
    print("Dejando de compartir pantalla")
    sleep(2)
    py.getWindowsWithTitle("Screen Sharing Meeting Controls")[0].maximize()
    py.hotkey('alt', 'S')
    sleep(1)

def write_chat(text):
    py.hotkey('alt', 'H')
    sleep(1)
    py.write(text)
    sleep(1)
    py.press("enter")