from flask import Flask, render_template, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random, string
import requests

app = Flask(__name__)

@app.route('/service3', methods=['GET'])
def service3():
  num=random.randint(1,8)
  return Response(str(num), mimetype='text/plain')

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5003, debug=True)
