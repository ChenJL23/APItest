# 通用断言方法
def comon_assert(self, resp, status_code, text):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(text, resp.text)
