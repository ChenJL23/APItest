import requests


class RbpLoginApi:
    # 发送登录请求
    @classmethod
    def login(cls, url, loging_data):
        resp = requests.post(url=f"{url}/auth/login", json=loging_data)
        return resp
