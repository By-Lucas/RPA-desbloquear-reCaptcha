# recaptcha libraries
import speech_recognition as sr
import pydub
import urllib
# import pydub
import urllib.request

import random
import os
import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def delay():
    time.sleep(random.dandint(2,3))

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=os.getcwd()+'\\chrome_driver\\chromedriver.exe')
driver.get("https://www.google.com/recaptcha/api2/demo")
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()
driver.switch_to.default_content()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='o desafio reCAPTCHA expira em dois minutos']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()


src=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.rc-audiochallenge-tdownload-link"))).click() #text

time.sleep(15)

#This does not work, it can't locate the src
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "audio-source")))
#Src_URL = driver.find_element_by_id('audio-source').get_attribute('src')

# get the mp3 audio file
#src = driver.find_element(By.ID, "audio-source").get_attribute("src")
#urllib.request.urlretrieve(src, "src.mp3")
print(src)

