from selenium import webdriver
import requests
import time

pageurl = 'https://www.google.com/recaptcha/api2/demo'

driver = webdriver.Chrome(executable_path=r'chrome_driver\chromedriver.exe')
driver.get(pageurl)

