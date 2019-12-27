from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 选择乘客 函数
def choicePassenger(driver):
	# 查看常用联系人
	driver.get('http://www.learnphp.com/index.html')
	# 保存常用联系人
	passengers = []
	choose = []
	while True:
		try:
			# 找到展示姓名的元素
			name_element = driver.find_elements_by_class_name('name-yichu')
			for x in name_element:
				passengers.append(x.text)
			# 翻页
			driver.find_element_by_class_name("next").click()
		except Exception as e:
			for i in range(len(passengers)):
				print('{0}-{1}'.format(i,passengers[i]))
			choose =  list(input("选择乘客（输入序号，多个用空格分隔）:，")\
				.split())		
			name = []
			for x in choose:
				name.append(passengers[x])
			return name


def queryTicket():
	stations = list(input("输入出发站和终点站（空格分隔）：").split())

# 打开浏览器
driver = webdriver.Firefox()
# 等待5秒
driver.implicitly_wait(5)
# a = choicePassenger(driver)
# print(a)
driver.get('http://www.baidu.com')
time.sleep(3)
driver.get('http://www.qq.com')
