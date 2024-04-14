import unittest

from htmltestreport import HTMLTestReport

from rbp import TestRBP
from test_rbp_login import TestRBPLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestRBP))

suite.addTest(unittest.makeSuite(TestRBPLogin))

report_path = 'reports/test_rbp.html'

# runner = HTMLTestReport(report_path, title='RBP测试报告', description='RBP登录测试报告')
runner = unittest.TextTestRunner()
runner.run(suite)
