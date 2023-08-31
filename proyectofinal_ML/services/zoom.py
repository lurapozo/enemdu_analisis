import pyautogui as py
from selenium import webdriver 
import time

def connect_zoom(meet_code, passcode):
    driver = webdriver.Chrome('C://Programs File/chorme/chromedriver.exe')
    driver.get('https://zoom.us/join')
      
    time.slee(5)
 
    driver.find_element_by_xpath("//input[@id='join-confno']").send_keys(meet_code)
 
    time.sleep(2)
    driver.find_element_by_xpath("//a[@id='btnSubmit']").click()
    time.sleep(5)
 
    enter_passcode = py.locateCenterOnScreen('passc.png')
    py.moveTo(enter_passcode)
    py.click()
    py.write(passcode)
 
    time.sleep(5)
    btn = py.locateCenterOnScreen("join.png")
    py.moveTo(btn)
    py.click()

def disconnect_zoom():
    pass