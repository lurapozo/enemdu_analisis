import pyautogui as py

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "C:\selenium_drivers\chromedriver" )
driver.maximize_window()

def connect_zoom(meet_code, password):
    driver.get(f"https://zoom.us/j/{meet_code}?pwd={password}")
    sleep(2)
    py.press("left")
    sleep(1)
    py.press("enter")
    sleep(2)
    driver.close()
    sleep(10)
    print("En Zoom")
    # share_screen()
    sleep(1)
    write_chat()
    sleep(1)
    disconnect_zoom()
    
def disconnect_zoom():
    print("Cerrando")
    py.hotkey('alt', 'Q')

def share_screen():
    py.hotkey('alt', 'S')
    sleep(1)
    py.press('enter')

def write_chat():
    py.hotkey('alt', 'H')
    sleep(1)
    py.write("Bienvenidos a la clase, comenzamos en segundos!!!")
    sleep(1)
    py.press("enter")