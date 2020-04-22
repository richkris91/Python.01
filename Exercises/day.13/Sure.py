from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import html
soup = BeautifulSoup(html)
app = Flask(__name__)
app.debug = True


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/', methods=['GET'])
def get_all():
    url = request.form['url']
    print(url)
    email = request.form['email']
    print(email)
    for res in soup.findAll('img'):
        print(res.get('src'))


app.run()
start()
