from flask import Flask, render_template, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random, string
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  final = requests.get('http://35.246.3.155:5004/service4')

  
  return render_template('home.html', output=final.text, title='Home' )


@app.route('/home/update', methods=['GET','POST'])
def update():
  data = requests.get('http://35.246.3.155:5002/service2')
  data1 = requests.get('http://35.246.3.155:5003/service3')
  final = data.text + data1.text
  return Response(final, mimetype='text/plain') 



if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
