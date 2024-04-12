import unittest

from htmltestreport import HTMLTestReport

from rbp import TestRBP

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestRBP))

report_path = 'reports/test_rbp.html'

runner = HTMLTestReport(report_path, title='RBP测试报告', description='RBP登录测试报告')
runner.run(suite)
