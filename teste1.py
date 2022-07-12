from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import os, sys
import time,requests
from bs4 import BeautifulSoup


delayTime = 2
audioToTextDelay = 10
filename = '1.mp3'
byPassUrl = 'https://www.google.com/recaptcha/api2/demo'
googleIBMLink = 'https://speech-to-text-demo.ng.bluemix.net/'
option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")

def audioToText(mp3Path):
    print("1")
    driver.execute_script('''window.open("","_blank");''')
    driver.switch_to.window(driver.window_handles[1])
    print("2")
    driver.get(googleIBMLink)
    delayTime = 10
    # Upload file
    time.sleep(1)
    print("3")
    # Upload file
    time.sleep(1)
    root = driver.find_element(By.ID,'root').find_elements(By.CLASS_NAME,'dropzone _container _container_large')
    btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
    btn.send_keys('D:/Lucas Programacao/26 freela -TRF-Webscraping-Captcha/TRF-Webscraping-Captcha/audios/1.mp3')
    # Audio to text is processing
    time.sleep(delayTime)
    #btn.send_keys(path)
    print("4")
    # Audio to text is processing
    time.sleep(audioToTextDelay)
    print("5")
    text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div').find_elements(By.TAG_NAME,'span')
    print("5.1")
    result = " ".join( [ each.text for each in text ] )
    print("6")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("7")
    return result
def saveFile(content,filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)


driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
driver.get(byPassUrl)
time.sleep(1)
googleClass = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
print(googleClass)
time.sleep(2)
outeriframe = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor")))
time.sleep(1)
outeriframe.click()
print('PASSOU 1')

time.sleep(2)
allIframesLen = driver.find_elements(By.TAG_NAME,'iframe')
print('PASSOU 2', allIframesLen)
time.sleep(1)
audioBtnFound = False
audioBtnIndex = -1
for index in range(len(allIframesLen)):
    driver.switch_to.default_content()
    iframe = driver.find_elements(By.TAG_NAME,'iframe')[index]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(delayTime)
    print('PASSOU 3',iframe)
    try:
        audioBtn = driver.find_element(By.ID,'recaptcha-audio-button') or driver.find_element(By.ID,'recaptcha-anchor')
        audioBtn.click()
        print('PASSOU 4')
        audioBtnFound = True
        audioBtnIndex = index
        break
    except Exception as e:
        print(e)
        pass

if audioBtnFound:
    try:
        while True:
            href = driver.find_element(By.ID,'audio-source').get_attribute('src')
            response = requests.get(href, stream=True)
            saveFile(response,filename)
            response = audioToText(os.getcwd() + '/' + filename)
            print(response)
            driver.switch_to.default_content()
            iframe = driver.find_elements(By.TAG_NAME,'iframe')[audioBtnIndex]
            driver.switch_to.frame(iframe)
            inputbtn = driver.find_element(By.ID,'audio-response')
            inputbtn.send_keys(response)
            inputbtn.send_keys(Keys.ENTER)
            time.sleep(2)
            errorMsg = driver.find_elements(By.CLASS_NAME,'rc-audiochallenge-error-message')[0]
            if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                print("Success")
                break
    except Exception as e:
            print(e)
            print('Caught. Need to change proxy now')
else:
    print('Button not found. This should not happen.')