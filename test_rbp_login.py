import unittest

from rbp_login_api import RbpLoginApi
from utils.assertUtil import comon_assert


class TestRBPLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = 'http://localhost:8080'

    def test01_login_ok(self):
        login = {
            'username': 'admin',
            'password': 'password'
        }
        resp = RbpLoginApi.login(self.url, login)
        print(f"登陆成功: {resp.status_code}")
        comon_assert(self, resp, 200, '')

    def test02_login_errPwd(self):
        login = {
            'username': 'admin',
            'password': '123'
        }
        resp = RbpLoginApi.login(self.url, login)
        print(f"登录失败: {resp.status_code}")
        comon_assert(self, resp, 403, '')


if __name__ == '__main__':
    unittest.main()
