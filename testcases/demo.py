import requests
from file.get_data import get_params


def login():
    url = "http://192.168.1.203:12999/api/token"
    raw_data = get_params()
    for j in range(len(raw_data)):
        result = requests.post(url=url, json=raw_data[j])
        print("第{times}组数据返回结果;".format(times=j + 1), result.text)


if __name__ == '__main__':
    login()

