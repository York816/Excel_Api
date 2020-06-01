# BeautifulReport报告方案：
import unittest
import time
from BeautifulReport import BeautifulReport

if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover(r"C:\PycharmProjects\ReadExcel/testcases", pattern="test_*.py")
    result = BeautifulReport(discover)
    nowtime = time.strftime("%Y%m%d%H%M%S")
    result.report(filename=f"report-" + nowtime, description="测试报告", report_dir="./reports")

# # HTMLTestRunner报告方案：
# import unittest, time
# from HTMLTestRunner import HTMLTestRunner
#
# test_case = r"C:\PycharmProjects\ReadExcel\testcases"  # 测试用例文件夹
# test_report = r"C:\PycharmProjects\ReadExcel\reports"  # 测试报告文件夹
# test_list = unittest.defaultTestLoader.discover(test_case, pattern='test*.py')
# if __name__ == '__main__':
#     nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
#     filename = test_report + '\\' + nowtime + 'result.html'
#     print(filename)
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner(stream=fp, title="selenium自动化测试报告",
#                             description="win10 chrome78 selenium3 + python3")
#     runner.run(test_list)
