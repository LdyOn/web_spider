"""导入requests模块，关于该模块的更多用法，参考官方文档：
http://docs.python-requests.org/zh_CN/latest/user/quickstart.html"""
import requests
import pygal
import time
from urllib.parse import quote

# #解决请求路径中含义中文或特殊字符
# url= quote('c++');
# print(url)
# exit()
def getData(keyword,page_size=1000):
	keyword = quote(keyword)
	url = "https://fe-api.zhaopin.com/c/i/sou?pageSize="+str(page_size)+\
	"&cityId=765&salary=0,0&workExperience=-1&education=-1&companyType" \
	"=-1&employmentType=-1&jobWelfareTag=-1&kw="+keyword+"&kt=3&_v=0.656" \
	"69009&x-zp-page-request-id=c29059bcab414d28a02023881dd" \
	"06e77-1552615114369-110766"
	headers = {
		'user-agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit\
		/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
		'Referer':'https://sou.zhaopin.com/?jl=765&sf=0&st=0&kw=java&kt=3',
		'Origin':'https://sou.zhaopin.com',
		'Accept':'application/json, text/plain, */*',
	}

	r = requests.get(url,headers = headers)
	# print(r.url)
	# exit()
	if r.status_code==200:
		data = r.json()
		return data['data']['numFound']
	else:
		print("获取关于"+str(keyword)+"的信息失败")
		print("code:",r.status_code)

def draw(data):
	bar_chart = pygal.Bar()
	bar_chart.add("Sort by language",list(data.values()))
	bar_chart.title = "深圳市热门开发语言在招职位统计，统计时间："+\
	time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	bar_chart.x_labels = list(data.keys())
	bar_chart.render_to_file("zhilian_jobs_count.svg")

count = {
	"java":0,
	"php":0,
	"python":0,
	"c语言":0,
	"c++":0,
	"android":0,
	"前端":0,
	"go语言":0,
}
languages = count.keys()
for lan in languages:
	total_num = getData(lan,page_size=1)
	count[lan] = total_num

#print(count)
draw(count)	
