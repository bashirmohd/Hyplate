from flask import Flask, render_template
from json import loads
from engine import *


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('hyplate/index.html')

@app.route('/register')
def register():
    return render_template('hyhub/oauth/register.html')

@app.route('/forgotpassword')
def forgotpassword():
    return render_template('hyhub/oauth/forgotpassword.html')

@app.route('/login')
def login():
    return render_template('hyhub/oauth/signin.html')

@app.route('/hyhub')
def hyhub():
    datainex = 'static/db/dataindex.json'
    with open(datainex, 'r+') as ff:
        lines = loads(ff.read())
    ff.close()
    return render_template('hyhub/hyhub.html', dataindex=lines)

@app.route('/infographics')
def infographics():
    return render_template('hyhub/infographics.html')

@app.route('/news')
def news():
    data = []
    news = 'static/db/newssources.json'
    with open(news, 'r+') as ff:
        lines = loads(ff.read())
    ff.close()
    for line in lines:
        articles = read_rss(line['feed'])
        for article in articles:
            article.update(line)
            data.append(article)
    shuffle(data)
    return render_template('hyplate/news.html', news=data)




