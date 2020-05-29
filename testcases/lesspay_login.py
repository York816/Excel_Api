import requests
from ReadExcle_api.file.get_data import getdate


def login():
    url = "http://192.168.1.203:12999/api/token"
    raw_data = getdate()
    # data = list(raw_data)
    for j in range(len(raw_data)):
        result = requests.post(url=url, json=raw_data[j])
        print("第{cishu}返回结果;".format(cishu=j + 1), result.text)


if __name__ == '__main__':
    login()
