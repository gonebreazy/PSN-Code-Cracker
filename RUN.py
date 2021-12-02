import random
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('store.playstation.com')
searchbox = driver.find_element_by_xpath('//*[@id="sb-social-toolbar-root"]/div/div/div[2]/div/button')
code = driver.find_element_by_xpath('//*[@id="sb-social-toolbar-root"]/div/div/div[2]/div/div[1]/ul/li[3]/button')
code_enter = driver.find_element_by_xpath('//*[@id="ember365"]')
code_enter.send_keys(code)

numbers = [1,2,3,4,5,6,7,8,9]
charz = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
code = ""

while True:
    print(code)
    code = random.choice(charz) + random.choice(charz) + random.choice(charz) + random.choice(
        charz) + random.choice(charz) + random.choice(charz) + random.choice(charz) + random.choice(
        charz) + random.choice(charz) + random.choice(charz) + random.choice(charz) + random.choice(charz)
