from flask import Flask, render_template, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random, string
import requests

app = Flask(__name__)
