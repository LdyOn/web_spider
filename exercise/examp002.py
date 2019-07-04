from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://wlsf.tpmission.com/#/login")
user_name = driver.find_element_by_xpath("//input[@type='text']")
user_name.clear
user_name.send_keys("admin")
pwd = driver.find_element_by_xpath("//input[@type='password']")
pwd.clear
pwd.send_keys("xxw15913132625")
driver.find_element_by_xpath("//button[@type='button']").click()




