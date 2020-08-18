from flask import Flask, render_template, Response
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random, string


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  
  return render_template('home.html', title='Home' )

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
  data = 'A2'
  if data == 'A2':
    output = "Hit"
  else:
    output = "Miss"

  return Response(output,mimetype='text/plain')

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
