from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 打开浏览器
driver = webdriver.Firefox()
# 等待5秒
driver.implicitly_wait(5)
# 登录
login(driver)
# 选择乘客，乘客姓名保存到列表里
passenger = choicePassenger(driver)
# 进入车票查询页
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
#出发站和终点站
station = list(input("请输入乘客姓名，空格分隔：").split())
#输入乘客姓名
passenger = list(input("请输入乘客姓名，多个用空格分隔：").split())


def login(driver):
	print("正在登录12306...")
	# 进入12306登录页
	driver.get("https://kyfw.12306.cn/otn/resources/login.html")
	
	time.sleep(4)

	js = 'var c = document.querySelectorAll(".login-hd-account > a:nth-child(1)");c[0].click();'
	# 执行js脚本选择账号密码登陆
	driver.execute_script(js)
	# 用户名
	login_name = input("输入用户名/邮箱/手机号：")
	# 登陆密码
	password = input("输入密码：")
	# 在表单中填入用户名和密码
	driver.find_element_by_id('J-userName').send_keys(login_name)
	driver.find_element_by_id('J-password').send_keys(password)
	#验证码图片
	img_code = driver.find_element_by_id('J-loginImg')
	#移动鼠标到验证码图片，
	action = webdriver.ActionChains(driver).\
	move_to_element_with_offset(img_code,0,0).perform()
	# 输入验证码选择
	select = list(map(int,input("请选择验证码图片(输入1-8，多张用空格分隔):").split()))
	"""将选择的图片序号转换为坐标，共有八张图片，
	第一张图片坐标大约为（40，40）,左右、上下间隔大约为70"""
	site = { 
		1 :(40,50),
		2 :(110,50),
		3:(180,55),
		4:(250,50),
		5:(40,120),
		6:(110,119),
		7:(183,125),
		8:(259,122),
	}
	# 逐个点击图片
	for x in select:
		webdriver.ActionChains(driver).move_to_element_with_offset(img_code,
			site[x][0],site[x][1]).click().perform()
	# 点击登录按钮
	driver.find_element_by_id('J-login').click()

# 选择乘客
def choicePassenger(driver):
	# 查看常用联系人
	driver.get('https://kyfw.12306.cn/otn/view/passengers.html')







