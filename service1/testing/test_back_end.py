import requests
import unittest 
from unittest.mock import patch

from flask import url_for
from flask_testing import TestCase
from service1.app import app

class TestBase(TestCase):
  def create_app(self):
    return app

class TestViews(TestBase):
  def test_home(self):
    response = self.client.get(url_for('home'))
    self.assertEquals(response.status_code,200)

  def test_update(self):
    response = self.client.get(url_for('update'))
    self.assertEquals(response.status_code,200)
