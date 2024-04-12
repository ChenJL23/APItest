import requests
import unittest

from parameterized import parameterized

from utils.readData import get_login_data


class TestIHrm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = "https://ihrm2-test.itheima.net/"

    @parameterized.expand(get_login_data())
    def test01_ihrm(self, unname, pwd, code, msg, expect):
        r = requests.get(self.url, json={})
