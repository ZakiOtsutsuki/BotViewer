import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = uc.Chrome()

def login(username, password):
    browser.get('https://google.com')
    browser.find_element(By.CSS_SELECTOR, '.gb_1').click()
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, '#identifierId').send_keys(username)
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)').click()
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, '#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys(password)
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)').click()
    time.sleep(3)
    print('successfully login')
    
def AutoPlayOff():
    browser.get('https://www.youtube.com/watch?v=Y2cRMoh-gAY')
    time.sleep(10)
    try:
        browser.find_element(By.CSS_SELECTOR, '#ad-text\:6').click()
    except:
        print('there is no ad')
    finally:
        browser.find_element(By.CSS_SELECTOR, '.ytp-autonav-toggle-button').click()
        print('autoplay is off')
    time.sleep(3)

def video(link):
    browser.get(link)
    wait = WebDriverWait(browser, 1000)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ytp-endscreen-next')))

login('arafiotsutsuki', 'zakiarafi')
AutoPlayOff()
view = 1
count = 0

while count < view:
    video('https://www.youtube.com/watch?v=Iem6SxpsS8s')
    video('https://www.youtube.com/watch?v=Y2cRMoh-gAY')
    video('https://www.youtube.com/watch?v=pE2j1W_QO0A')
    video('https://www.youtube.com/watch?v=Z_G_BpPzGIE')
    video('https://www.youtube.com/watch?v=VLpFgay9ZWY')
    video('https://www.youtube.com/watch?v=UFwQZ7od4tY')
    count = count + 1
    print('view count:', count)