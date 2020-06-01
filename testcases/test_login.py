import unittest
import time
import requests
from file.get_data import get_params


class Test(unittest.TestCase):

    def setUp(self):
        print("准备开始执行{}测试用例...".format(self))

    def tearDown(self):
        print("测试已结束，输出log完结...\n")

    def test_gettoken(self):  # 获取token测试用例
        url = "http://192.168.1.203:12999/api/token"
        raw_data = get_params()
        # data = list(raw_data)
        for j in range(len(raw_data)):
            result = requests.post(url=url, json=raw_data[j])
            print("第{cishu}组数据返回结果：".format(cishu=j + 1), result.text)
            time.sleep(0.5)

    def test_out1(self):  # 测试多条用例
        print("hello 1")

    def test_out2(self):
        print("hello 2")


if __name__ == '__main__':
    unittest.main()
