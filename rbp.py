import unittest
import requests


class TestRBP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = 'http://localhost:8080'

    def test01_rbp_login(self):
        login = {
            'username': 'admin',
            'password': 'password'
        }
        res = requests.post(self.url + '/auth/login', json=login)
        print(res.status_code)

        self.assertEqual(200, res.status_code)

    def test02_rbp_login(self):
        login = {
            'username': 'admin',
            'password': 'admin'
        }
        res = requests.post(self.url + '/auth/login', json=login)
        print(res.status_code)

        self.assertEqual(403, res.status_code)


if __name__ == '__main__':
    unittest.main()
