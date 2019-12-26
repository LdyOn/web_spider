from selenium import webdriver
import time

# 打开浏览器
driver = webdriver.Firefox()
# 等待5秒
driver.implicitly_wait(5)
driver.get("https://kyfw.12306.cn/otn/resources/login.html")
time.sleep(3)
js = 'var u_o = document.querySelectorAll(".login-hd-account > a:nth-child(1)");u_o[0].click();'
# 执行js脚本选择账号密码登陆
driver.execute_script(js)
#验证码图片
img_code = driver.find_element_by_id('J-loginImg')

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