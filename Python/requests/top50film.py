import requests

for i in range(2):
    top_url = 'https://movie.douban.com/top250?start=0&filter='.format(i*25)