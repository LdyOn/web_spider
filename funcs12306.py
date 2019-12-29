import time
import random

# 登录函数
def login(driver):
	print("正在登录12306...")
	# 进入12306登录页
	driver.get("https://kyfw.12306.cn/otn/resources/login.html")
	
	time.sleep(1)

	
	# 执行js脚本选择账号密码登陆
	try:
		driver.execute_script('var c = document.querySelectorAll\
			(".login-hd-account > a:nth-child(1)");c[0].click();')
	except Exception as e:
		return False
	
	# 用户名
	login_name = input("输入用户名/邮箱/手机号：")
	# 登陆密码
	password = input("输入密码：")
	# 在表单中填入用户名和密码
	driver.find_element_by_id('J-userName').send_keys(login_name)
	driver.find_element_by_id('J-password').send_keys(password)
	#验证码图片
	img_code = driver.find_element_by_id('J-loginImg')
	# 输入验证码选择
	select = list(map(int,input("请选择验证码图片(输入1-8，多张用空格分隔):").split()))
	"""将选择的图片序号转换为坐标，共有八张图片，
	第一张图片坐标大约为（40，50）,左右、上下间隔大约为70，下面是八张图片
	的近似点击坐标"""
	site = { 
		1 :(40,68),
		2 :(110,67),
		3:(180,65),
		4:(250,59),
		5:(40,132),
		6:(110,129),
		7:(183,135),
		8:(259,132),
	}

	# 逐个点击图片
	for x in select:
		webdriver.ActionChains(driver).move_to_element_with_offset(img_code,
			site[x][0],site[x][1]).click().perform()

	time.sleep(6)

	# 点击登录按钮
	driver.find_element_by_id('J-login').click()

	return True

# 选择乘客
def choose_passenger(driver):
	# 查看常用联系人
	driver.get('https://kyfw.12306.cn/otn/view/passengers.html')
	# 保存常用联系人
	passengers = []
	choose = []
	while True:
		try:
			# 找到展示姓名的元素
			name_element = driver.find_elements_by_class_name('name-yichu')
			for x in name_element:
				passengers.append(x.text)
			# 写一段js进行翻页
			js = 'var next = document.getElementsByClassName("next");\
			next[0].click();'
			driver.execute_script(js)
			time.sleep(2)
		except Exception as e:
			print("乘客信息如下：")
			for i in range(len(passengers)):
				print('{0:3}  {1:5}'.format(i,passengers[i]))
			choose =  list(map(int,input("选择乘客（输入名字前的序号，多个用空格分隔）:")\
				.split()))		
			name = []
			for x in choose:
				name.append(passengers[x])

			return name


# 查询车票
def  query_tickets(driver,travel_dates):

	# 设置出发日
	driver.execute_script('document.getElementById("train_date").removeAttribute("readonly");')
	date = driver.find_element_by_id('train_date')
	date.clear()
	date.send_keys(travel_dates[random.randint(0,len(travel_dates))])
	# 点击查询
	driver.execute_script('document.getElementById("query_ticket").click();')

	time.sleep(1)


# 选择车次
def choose_train(driver):
	trains = {}
	train_number = driver.find_elements_by_class_name('number')
	s_time = driver.find_elements_by_class_name('start-t')
	length = len(train_number)
	for i in range(length):
		trains[train_number[i].text] = s_time[i].text

	print("{0:6} {1:6}".format("车次","出发时间"))
	for x in trains.items():
		print("{0:6} {1:6}".format(x[0],x[1]))
	return list(input("选择车次，多个用空格分隔：").split())

# 判断是否有票
def can_buy(driver,train_number,passenger_num,seat_level):

	js ='var tb = document.getElementById("queryLeftTable");\
		var rows = tb.children;\
		var train_number = '+train_number+';\
		var passenger_num = '+passenger_num+';\
		var seat_level = '+seat_level+';\
		var length = rows.length;\
		for (var i = 0; i <length; i++) {\
			if(rows[i].children.length==0)continue;\
			var number = rows[i].children[0].children[0]\
			.children[0].children[0].textContent.trim();\
			if(train_number.indexOf(number)==-1)\
				continue;\
			for (var j = seat_level.length - 1; j >= 0; j--) {\
				if(rows[i].children[seat_level[j]].textContent == "有"){\
					rows[i].lastElementChild.firstChild.click();\
				}\
				if(rows[i].children[seat_level[j]].textContent >=passenger_num){\
					rows[i].lastElementChild.firstChild.click();\
				}\
			}\
		}'
	driver.execute_script(js)

# 点击下单，确认购买
def confirm_buy(driver, passengers):
	ticket = driver.find_element_by_id("ticket_tit_id")
	print("".format(ticket.text))
	js='var passengers='+list_to_string(passengers)+';\
		var passengers_list = document.getElementById("normal_passenger_id");\
		var li = passengers_list.children;\
		var length = li.length;\
		for(var i = 0;i<length;i++){\
			if(passengers.indexOf(li.children[1].textContent)==-1){\
				continue;\
			}\
			li.children[0].click();\
		};\
		document.getElementById("submitOrder_id").click()\
	'
	driver.execute_script(js)

	print("订单已提交，请登录12306完成支付")
	#接下来可以发送邮件通知


def list_to_string(li):
	t_n = ""
	for x in li:
		t_n += '"'+x+'",'
	t_n = '['+t_n+']'

	return t_n