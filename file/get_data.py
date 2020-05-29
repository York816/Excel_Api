import xlrd


def getdate():
    files = xlrd.open_workbook(r'C:\PycharmProjects\Read ini\ReadExcleDate\file\Login_data.xlsx',
                               encoding_override="utf-8")
    sheet1 = files.sheet_by_name('login_api')  # 指定sheet页
    sheet1rows = sheet1.nrows  # 获取总行数
    api_list = []
    value = ''
    # 将登录参数以列表数据返回
    for i in range(1, sheet1rows):
        value = sheet1.row_values(i)
        date = {
            "email": value[0],
            "password": value[1]
        }
        api_list.append(date)
    return api_list


if __name__ == '__main__':
    getdate()
    print(getdate())
