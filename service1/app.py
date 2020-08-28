from flask import Flask, render_template, Response, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random, string
import requests




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
db = SQLAlchemy(app)


class Output(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  coordinates = db.Column(db.String(10))


  def __repr__(self):
    return ' '.join(['Coordinates:', self.coordinates])


@app.route('/')
@app.route('/home')
def home():
  
  data = requests.get('http://service4:5004/service4')
  postData=Output.query.all() 
  
  
  return render_template('home.html',maybe=data.text, posts=postData ,title='Home' )


@app.route('/home/update', methods=['GET','POST'])
def update():
  data = requests.get('http://service2:5002/service2')
  data1 = requests.get('http://service3:5003/service3')
  final = data.text + data1.text
  coordinate1 = Output(coordinates=final)
  db.session.add(coordinate1)
  db.session.commit()
  return Response(final, mimetype='text/plain') 


@app.route('/home/delete', methods=['GET','POST'])
def delete():
  update = db.session.query(Output).delete()
  db.session.commit()
  return redirect(url_for('home'))

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)






