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
    time.sleep(random.randint(2,3))

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=os.getcwd()+'\\chrome_driver\\chromedriver.exe')
driver.get("https://www.google.com/recaptcha/api2/demo")

# Switch  to recaptcha frame
frames=driver.find_elements(By.TAG_NAME,"iframe")
driver.switch_to.frame(frames[0]);
delay()

# Switch on checkbox to activate recaptcha
driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()

#Swuitch to recaptcha audio control frame
driver.switch_to.default_content()
frames=driver.find_element(By.XPATH,'/html/body/div[2]/div[4]').find_elements(By.TAG_NAME,"iframe")
driver.switch_to.frame(frames[0])
delay()

#click on audio challenge
driver.find_element(By.ID, "recaptcha-audio-button").click()

#Switch to recaptcha aidop challenge frame
driver.switch_to.default_content()
frames=driver.find_elements(By.TAG_NAME,"iframe")
driver.switch_to.frame(frames[-1])
delay()

#Click on the play buttom
driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/button").click()