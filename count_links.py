"""这是一个简单的脚本，用递归的方式统计某个站点的所有链接"""
from bs4 import BeautifulSoup
import requests
import re

def count_link(entrance):
	links = [entrance] #保存所有链接
	trace = [] #已统计过的页面
	stack = [entrance]#带统计的页面
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit"\
		"/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
		
	}
	while len(stack):
		latest_link = stack.pop()
		if latest_link in trace:
			continue
		
		r = requests.get(latest_link,headers=headers)
		# print(r.text)
		# exit()
		if r.status_code==200:
			soup = BeautifulSoup(r.text,"lxml")
			for a in soup.find_all('a'):
				link = a.get("href")
				m=re.match(r'(https?:(//[a-z0-9]+\.[a-z0-9]+\.[a-z]+)).*(\.html|\.php|\.htm)(\?\w)?',
					link)  
				if m and m.groups()[0]==entrance:
					if link not in links:
						links.append(link)
						print(link)
						with open("links.txt","a+") as f:
							f.write(link+"\n")
					if link not in stack:
						stack.append(link)
				# elif m and re.match(m.groups[1],link):
				# 	link = entrance + link
				# 	if link not in links:
				# 		links.append(link)
				# 		print(link)
				# 		with open("links.txt","a") as f:
				# 			f.write(link)
				# 	if link not in stack:
				# 		stack.append(link)
				elif re.match(r'/[^/]+.*',link):
					link = entrance + link
					if link not in links:
						links.append(link)
						print(link)
						with open("links.txt","a") as f:
							f.write(link+"\n")
					if link not in stack:
						stack.append(link)
					
		print(stack)
		trace.append(latest_link)
	return links
#运行函数
count = count_link("http://www.baidu.com")
# print(count)			
