import pyautogui as py
import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

def connect_zoom(meet_code, password):
    # Example = https://us04web.zoom.us/j/77943644084?pwd=TWI0WS91b3dqUG1Jd1hUQkFzYTh0QT09
    driver.get(f"https://zoom.us/j/{meet_code}?pwd={password}")
    driver.maximize_window()
    time.sleep(2)
    alert = Alert(driver)
    alert.dismiss()
    # Cambiar el tiempo de espera dependiendo del rendimiento de tu maquina.
    time.sleep(8)
    py.press('c')
    time.sleep(1)
    py.write("Bienvenidos a la clase, comenzamos en segundos!!!")
    time.sleep(1)
    py.press("enter")
      
def disconnect_zoom():
    py.press('q')
    time.sleep(1)
    py.moveTo(683,362)
    time.sleep(1)
    py.click()