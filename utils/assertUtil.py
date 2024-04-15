# 通用断言方法
def comon_assert(self, resp, status_code, text):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(text, resp.text)


def common_assert(self, resp, status_code, success, code, message):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(success, resp.json().get("success"))
    self.assertEqual(code, resp.json().get("code"))
    self.assertIn(message, resp.json().get("message"))
