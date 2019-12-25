from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 打开浏览器
driver = webdriver.Firefox()
# 打开12306官网
driver.get("https://www.12306.cn/index/")
# 等待5秒
driver.implicitly_wait(5)
# 等待加载后，找到登陆按钮
login_link = driver.find_element_by_xpath("//li[@id='J-header-login']/a[1]")
# 点击进入登录页面
webdriver.ActionChains(driver).move_to_element(login_link ).click(login_link ).perform()
# 等待四秒
driver.implicitly_wait(4)
# 点击“账号登陆”，选择用账号密码登陆
driver.find_element_by_link_text('账号登陆').click()
# 用户名
login_name = input("输入用户名/邮箱/手机号：")
# 登陆密码
password = input("输入密码：")
# 在表单中填入用户名和密码
driver.find_element_by_id('J-userName').send_keys(login_name)
driver.find_element_by_id('J-password').send_keys(password)










