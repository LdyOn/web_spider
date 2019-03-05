import requests
from bs4 import BeautifulSoup

def get_movies():
	headers = {
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) \
		Gecko/20100101 Firefox/65.0',
		'Host':'movie.douban.com',

	}
	movie_list = []
	for i in range(0,10):
		link = 'https://movie.douban.com/top250?start='+str(i*25)
		r = requests.get(link, headers=headers,timeout=10)
		print(str(i+1),"页响应状态吗:",r.status_code)
		# print(r.text)
		soup = BeautifulSoup(r.text,"html.parser")
		div_list = soup.find_all('div', class_='hd')
		for each in div_list:
			movie = each.a.span.text.strip()
			movie_list.append(movie)
	return movie_list

movies = get_movies()
print(movies)