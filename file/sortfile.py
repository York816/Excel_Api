import os, glob, time


# def findfinally(path):
#     s = sorted(glob.glob(os.path.join(path, '*')),
#                key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(x))),
#                reverse=True)
#     return s[0]

# 输出最新的报告
def findfinally(path):
    s = sorted(glob.glob(os.path.join(path, '*')),
               key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(x))), reverse=True)

    return s[0]
    # pathfile = os.path.dirname(s[0])  # 截取文件名
    # return s[0][len(pathfile) + 1:]


if __name__ == '__main__':
    print(findfinally(r"C:\PycharmProjects\ReadExcel\reports"))
