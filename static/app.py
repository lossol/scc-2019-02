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

## HTML을 주는 부분

@app.route('/popup')
def test():
    return jsonify({'result': 'success'})

# @app.route('/')
# def home():
#    return render_template('index.html')


@app.route('/save', methods=['POST'])
def save():
    url_receive = ''

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/bi/mi/basic.nhn?code=174903#', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')



    return jsonify({'result':'success'})


def movies(args):
    pass


@app.route('/get', methods=['GET'])
def get():
    # movies = db.genie.find({}, {'_id': 0})
    return jsonify({'result': 'success', 'movies': list(movies)})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)