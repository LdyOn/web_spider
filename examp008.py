import requests
import json
from pymongo import  MongoClient


client = MongoClient('localhost',27017)
db = client.zhihu_database
collection = db.live

def scrapy(link):
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
		AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.\
		3578.98 Safari/537.36',
		'Host':'api.zhihu.com',
		'Origin':'https://www.zhuhu.com',
		'Referer':'https://www.zhihu.com/lives',
		'authority':'api.zhihu.com',

	}
	r = requests.get(link, headers=headers)
	return r.text
link = "https://api.zhihu.com/lives/homefeed?includes=live"
is_end = False
while not is_end:
	html = scrapy(link)
	decodejson = json.loads(html)
	collection.insert_one(decodejson)
	link = decodejson['paging']['next']
	is_end = decodejson['paging']['is_end']