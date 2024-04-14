import unittest
import requests


class TestRBP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = 'http://localhost:8080'

    # 登录成功
    def test01_rbp_login(self):
        login = {
            'username': 'admin',
            'password': 'password'
        }
        res = requests.post(self.url + '/auth/login', json=login)
        print(res.status_code)
        print(res.text)

        self.assertEqual(200, res.status_code)
        self.assertEqual('', res.text)

    # 密码错误
    def test02_rbp_login(self):
        login = {
            'username': 'admin',
            'password': 'admin'
        }
        res = requests.post(self.url + '/auth/login', json=login)
        print(res.status_code)
        print(res.text)

        self.assertEqual(403, res.status_code)
        self.assertEqual('', res.text)


if __name__ == '__main__':
    unittest.main()
