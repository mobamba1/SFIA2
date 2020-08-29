import requests
import unittest 
from unittest.mock import patch

from flask import url_for
from flask_testing import TestCase
from service1.app import app
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLACHEMY_DATABASE_URI=getenv('DATABASE_URI'),
                SECRET_KEY=getenv('SKEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

class TestViews(TestBase):                                             

  def test_delete(self):
    response = self.client.get(url_for('delete'))
    self.assertEquals(response.status_code,302)


  def test_home1(self):
    with patch('requests.get') as g:
       g.return_value.text = 'Miss'
       response = self.client.get(url_for('home'))
       self.assertEquals(response.status_code,200)

  def test_home2(self):
    with patch('requests.get') as g:
       g.return_value.text = 'hit'
       response = self.client.get(url_for('home'))
       self.assertEquals(response.status_code,200)


  def test_update(self):
    with patch('requests.get') as g:
       g.return_value.text = 'A'
       response = self.client.get(url_for('update'))
       self.assertEquals(response.status_code,200)
       
