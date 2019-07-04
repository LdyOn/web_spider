"""深度优先搜索爬取wikipedia首页链接，depth=2"""
import requests
import re
import time
from bs4 import BeautifulSoup

time1 = time.time()
exist_url = []
g_writecount = 0

def scrappy(url,depth=1):
	global g_writecount
	try:		
		headers = {
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
			AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.\
			3578.98 Safari/537.36',
		}

		r = requests.get("https://en.wikipedia.org/wiki/"+url,
			headers = headers)

		html = r.text
	except Exception as e:
		print('Failed downloading and saving',url)
		print(e)
		return None

	exist_url.append(url)
	link_list = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>',html)
	unique_list = list(set(link_list)-set(exist_url))
	for eachone in unique_list:
		g_writecount +=1
		output = "No." + str(g_writecount) +"\t Depth"+str(depth)+\
			"\t" +url+' ->'+eachone+'\n'
		print(output)
		with open('title.txt',"a+") as f:
			f.write(output)
			f.close()
		if depth < 2:
			scrappy(eachone,depth+1)
scrappy("wikipedia")
time2 = time.time()
print("Total time",time2-time1)



# bsobj = BeautifulSoup(html)
# for link in bsobj.findAll("a"):
# 	if 'href' in link.attrs:
# 		print(link.attrs['href'])