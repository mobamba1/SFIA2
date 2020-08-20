from flask import Flask, render_template, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random, string
import requests

app = Flask(__name__)

@app.route('/service2', methods=['GET'])
def service2():
  list1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
  b=random.randint(0,7)
  return Response(list1[b], mimetype='text/plain')

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5002, debug=True)
