from flask import Flask, render_template, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random, string
import requests

app = Flask(__name__)

@app.route('/service4', methods=['GET','POST'])
def service4():
  data1 = requests.get('http://34.105.244.35:5000/home/update')
  if data1.text == 'A2' or data1.text == 'A1' or data1.text == 'A3' or data1.text == 'A4' or data1.text == 'A5' or data1.text == 'A6' or data1.text == 'A7' or data1.text == 'A8':
    output = "Hit"
  else:
    output = "Miss"
  
  return Response(output,mimetype='text/plain')

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5004, debug=True)
