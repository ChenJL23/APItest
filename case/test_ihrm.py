import requests
import unittest

from parameterized import parameterized

from utils.assertUtil import common_assert
from utils.readData import get_data


class TestIHrm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = "https://ihrm2-test.itheima.net"

    @parameterized.expand(get_data('/data/ihrm_login.json'))
    def test01_ihrm(self, phone, pwd, code, msg):
        req_body = {
            "mobile": phone,
            "password": pwd
        }
        r = requests.post(self.url + '/api/sys/login', json=req_body)
        print(r.json())
        common_assert(self, r, 200, True, code, msg)


if __name__ == '__main__':
    unittest.main()
