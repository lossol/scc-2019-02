# 방으로 만들어서,라우터를 만들어서 ajx로 연결
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


articles = []
article_no = 1
# url_receive = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190715'

@app.route('/popup')
def test():
    return jsonify({'result': 'success'})

@app.route('/')
def home():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/bi/mi/basic.nhn?code=174903#', headers=headers)
    # 코드가 유동적인거지!
    soup = BeautifulSoup(data.text, 'html.parser')

    src = soup.select_one('div.article > div.mv_info_area > div.poster > a > img')
    # content > div.article > div.mv_info_area > div.poster > a > img

    title = soup.select_one('div.mv_info_area>div.mv_info>h3>a').text
    print(title)
    directors = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a')
    # director = [];

    for a in directors:
        print(a.text)

    actors = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p > a')
    # actor = [];

    for a in actors:
        print(a.text)

    dates = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4)')
    # date = [];

    for a in dates:
        print(a.text)

    subtitle = soup.select_one(
        'div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > h5').text
    story = soup.select_one(
        'div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > p').text

    print(subtitle)
    print(story)

    return render_template('index.html')


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)