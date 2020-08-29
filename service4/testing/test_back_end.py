import requests
import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from service4.app import app
class TestBase(TestCase):
  def create_app(self):
    return app
class TestViews(TestBase):
  def test_home(self):
     with patch('requests.get') as g:
       g.return_value.text = "A1"
       response = self.client.get(url_for('service4'))
       self.assertEquals(response.status_code,200)
       

  def test_hit(self):
     with patch('requests.get') as g:
       g.return_value.text = "A1"

       response = self.client.get(url_for('service4'))
       self.assertIn(b'Hit', response.data)
  def test_hit1(self):
     with patch('requests.get') as g:
       g.return_value.text = "A2"

       response = self.client.get(url_for('service4'))
       self.assertIn(b'Hit', response.data)

  def test_hit3(self):
     with patch('requests.get') as g:
       g.return_value.text = "A3"

       response = self.client.get(url_for('service4'))
       self.assertIn(b'Hit', response.data)

  def test_hit4(self):
     with patch('requests.get') as g:
       g.return_value.text = "A4"

       response = self.client.get(url_for('service4'))
       self.assertIn(b'Hit', response.data)

  def test_hit5(self):
     with patch('requests.get') as g:
       g.return_value.text = "A5"

       response = self.client.get(url_for('service4'))
       self.assertIn(b'Hit', response.data)

  def test_hit6(self):
     with patch('requests.get') as g:
       g.return_value.text = "A6"

       response = self.client.get(url_for('service4'))
       self.assertIn(b'Hit', response.data)

  def test_hit7(self):
     with patch('requests.get') as g:
       g.return_value.text = "A7"

       response = self.client.get(url_for('service4'))
       self.assertIn(b'Hit', response.data)

  def test_hit8(self):
     with patch('requests.get') as g:
       g.return_value.text = "A8"

       response = self.client.get(url_for('service4'))
       self.assertIn(b'Hit', response.data)

  def test_miss(self):
     with patch('requests.get') as g:
       g.return_value.text = "B1"
       response = self.client.get(url_for('service4'))
       self.assertIn(b'Miss', response.data)
