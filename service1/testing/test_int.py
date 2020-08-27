import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from service1.app import app, db


class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('DATABASE_URI'))
        app.config['SECRET_KEY'] = getenv('SKEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/kenneth1521412/SFIA2/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://34.89.28.103:5000/")
        
        db.session.commit()
        

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://34.89.28.103:5000")
        self.assertEqual(response.code, 200)


class TestView(TestBase):
    def test_coordinate(self):
        self.driver.find_element_by_xpath('/html/body/form[1]/button').click()
        time.sleep(1)
        assert url_for('home') in self.driver.current_url

    def test_delete(self):
        self.driver.find_element_by_xpath('/html/body/form[2]/button').click()
        time.sleep(1)
        assert url_for('home') in self.driver.current_url




if __name__ == '__main__':
    unittest.main(port=5000)

