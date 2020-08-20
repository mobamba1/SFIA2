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


@app.route('/service2', methods=['GET'])
def service2():
  list1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
  b=random.randint(0,7)

  return Response(list1[b], mimetype='text/plain')

@app.route('/service3', methods=['GET'])
def service3():
  num=random.randint(1,8)
	
  return Response(str(num), mimetype='text/plain')

@app.route('/service4', methods=['GET','POST'])
def service4():
  data = requests.get('http://35.246.3.155:5000/home/update')
  if data.text == 'A2' or data.text == 'A1' or data.text == 'A3' or data.text == 'A4' or data.text == 'A5' or data.text == 'A6' or data.text == 'A7' or data.text == 'A8':
    output = "Hit"
  else:
    output = "Miss"

  return Response(output,mimetype='text/plain')

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
