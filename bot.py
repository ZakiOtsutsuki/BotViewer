import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
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
    time.sleep(10)

def video(link, t):
    browser.get(link)
    time.sleep(t)

login('naruto1745uzumaki', 'arafi1745')
view = 1
count = 0

while count < view:
    video('https://www.youtube.com/watch?v=Iem6SxpsS8s', 240)
    video('https://www.youtube.com/watch?v=Y2cRMoh-gAY', 780)
    video('https://www.youtube.com/watch?v=pE2j1W_QO0A', 840)
    video('https://www.youtube.com/watch?v=Z_G_BpPzGIE', 120)
    video('https://www.youtube.com/watch?v=VLpFgay9ZWY', 120)
    video('https://www.youtube.com/watch?v=UFwQZ7od4tY', 180)
    count = count + 1