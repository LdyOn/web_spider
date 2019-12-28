# -*- coding: UTF-8 -*-
# python购票脚本
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# 查询车票
def  query_tickets(driver,travel_dates):

	# 设置出发日
	driver.execute_script('document.getElementById("train_date").removeAttribute("readonly");')
	date = driver.find_element_by_id('train_date')
	date.clear()
	date.send_keys(travel_dates[random.randint(0,len(travel_dates)-1)])
	# 点击查询
	driver.execute_script('document.getElementById("query_ticket").click();')

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
			console.log(rows[i].children);\
			console.log(seat_level);\
			for (var j = seat_level.length - 1; j >= 0; j--) {\
				if(rows[i].children[seat_level[j]].textContent == "有"){\
					rows[i].lastElementChild.firstChild.click();\
				}\
				if(rows[i].children[seat_level[j]].textContent >=passenger_num){\
					rows[i].lastElementChild.firstChild.click();\
				}\
			}\
		}'
	print(js)
	driver.execute_script(js)

# 打开浏览器
driver = webdriver.Firefox()
# 等待5秒
driver.implicitly_wait(5)
# 进入车票查询页
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

# 设置出发地
s = driver.find_element_by_id('fromStationText')
ActionChains(driver).move_to_element(s)\
.click(s)\
.send_keys_to_element(s,'北京')\
.move_by_offset(20,50)\
.click()\
.perform()

# 设置目的地
e = driver.find_element_by_id('toStationText')
ActionChains(driver).move_to_element(e)\
.click(e)\
.send_keys_to_element(e,'南京')\
.move_by_offset(20,50)\
.click()\
.perform()

query_tickets(driver,["2020-01-17"])

train_number = choose_train(driver)

t_n = ""

for x in train_number:
	t_n += '"'+x+'",'
train_number = '['+t_n+']'

seat_level = [2,3,7,9]

seat_level = ",".join(str(i) for i in seat_level)

seat_level = '['+seat_level+']'
# time.sleep(5)
can_buy(driver,train_number,"2",seat_level)


