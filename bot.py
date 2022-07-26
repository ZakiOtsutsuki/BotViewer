import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

browser = uc.Chrome()

username = 'zakijamaliarafi'
password = 'zaki1745'

def login():
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

login()