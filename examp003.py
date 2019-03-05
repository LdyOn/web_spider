from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time

caps = webdriver.DesiredCapabilities().FIREFOX
caps['marionette'] = False
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)

driver.get("http://www.baidu.com")
user_name = driver.find_element_by_xpath("//form[1]/input[1]")
print(user_name.placeholder)

