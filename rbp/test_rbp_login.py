import unittest

from parameterized import parameterized

from rbp.rbp_login_api import RbpLoginApi
from utils.assertUtil import comon_assert
from utils.readData import get_data


class TestRBPLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = 'http://localhost:8080'

    # def test01_login_ok(self):
    #     req_body = {
    #         'username': 'admin',
    #         'password': 'password'
    #     }
    #     resp = RbpLoginApi.login(self.url, req_body)
    #     print(f"登陆成功: {resp.status_code}")
    #     comon_assert(self, resp, 200, '')
    #
    # def test02_login_errPwd(self):
    #     req_body = {
    #         'username': 'admin',
    #         'password': '123'
    #     }
    #     resp = RbpLoginApi.login(self.url, req_body)
    #     print(f"登录失败: {resp.status_code}")
    #     comon_assert(self, resp, 403, '')

    # 测试数据参数化
    @parameterized.expand(get_data('../data/rbp_login.json'))
    def test_login(self, user, pwd, code, text):
        req_body = {
            'username': user,
            'password': pwd
        }
        resp = RbpLoginApi.login(self.url, req_body)
        comon_assert(self, resp, code, text)


if __name__ == '__main__':
    unittest.main()
