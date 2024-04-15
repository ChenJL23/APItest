import requests


class RbpLoginApi:
    # 发送登录请求
    @classmethod
    def login(cls, url, req_body):
        resp = requests.post(url=f"{url}/auth/login", json=req_body)
        return resp
