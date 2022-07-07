from selenium.webdriver.common.keys import Keys

# recaptcha libraries
import speech_recognition as sr
import urllib
# import pydub
import urllib.request

import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r'chrome_driver/chromedriver.exe')
driver.get("https://www.google.com/recaptcha/api2/demo")
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()
driver.switch_to.default_content()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='o desafio reCAPTCHA expira em dois minutos']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()

# get the mp3 audio file
src = driver.find_element(By.ID, "audio-source").get_attribute("src")
urllib.request.urlretrieve(src, "src.mp3")
print(src)