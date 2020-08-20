from flask import Flask, render_template, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random, string
import requests

app = Flask(__name__)

@app.route('/service4', methods=['GET','POST'])
def service4():
  data = requests.get('http://35.246.3.155:5000/home/update')
  if data.text == 'A2' or data.text == 'A1' or data.text == 'A3' or data.text == 'A4' or data.text == 'A5' or data.text == 'A6' or data.text == 'A7' or data.text == 'A8':
    output = "Hit"
  else:
    output = "Miss"
  return Response(output,mimetype='text/plain')

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5004, debug=True)
