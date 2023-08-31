import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

def moves_to_slides(link_ppt, class_name):
    driver.get(link_ppt)
    driver.maximize_window()
    print("Esperando a que abra el navegador web....")
    time.sleep(2)
    slides = driver.find_elements(By.CLASS_NAME, class_name)
    num_slides = len(slides)
    for index in range(num_slides - 1):
        slides[index].click()
        # pyautogui.click(x = 100, y = 100)
        time.sleep(1)
