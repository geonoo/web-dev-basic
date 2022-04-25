import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:test@cluster0.lommb.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#영화제목 #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#평점 #old_content > table > tbody > tr:nth-child(2) > td.point
#순위 #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    title = movie.select_one('td.title > div > a')
    score = movie.select_one('td.point')
    rank = movie.select_one('td:nth-child(1) > img')
    if title is not None:
        print(title.text, score.text, rank['alt'])
        doc = {
            'title':title.text,
            'rank':rank['alt'],
            'score':score.text
        }
        db.movies.insert_one(doc)

