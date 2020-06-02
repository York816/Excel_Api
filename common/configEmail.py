import os
import win32com.client as win32  # python -m pip install pypiwin32
import datetime
from file.sortfile import findfinally

# from common import readConfig
# from common import getpathInfo
# read_conf = readConfig.ReadConfig()
# subject = read_conf.get_email('subject')  # 从配置文件中读取，邮件主题
# app = str(read_conf.get_email('app'))  # 从配置文件中读取，邮件类型
# addressee = read_conf.get_email('addressee')  # 从配置文件中读取，邮件收件人
# cc = read_conf.get_email('cc')  # 从配置文件中读取，邮件抄送人
# mail_path = os.path.join(getpathInfo.get_Path(), 'results', 'report*.html')  # 获取测试报告路径
subject = '接口测试报告'
app = 'Outlook'
addressee = "York.Ye@songmao.tech"
cc = "york816@163.com"
# mail_path = os.path.join(r'C:\PycharmProjects\ReadExcel', 'reports', 'report-20200601122739.html')
mail_path = findfinally(r"C:\PycharmProjects\ReadExcel\reports")  # 返回最新的一份报告


def outlook():
    # olook = win32.Dispatch("%s.Application" % app)
    # mail = olook.CreateItem(win32.constants.olMailItem)  # 此方法调用不了，改写下面方式
    outlook = win32.Dispatch("%s.Application" % app)  # 固定写法
    mail = outlook.CreateItem(0)  # 固定写法
    mail.To = addressee  # 收件人
    mail.CC = cc  # 抄送
    mail.Subject = str(datetime.datetime.now())[0:19] + '%s' % subject  # 邮件主题
    mail.Attachments.Add(mail_path, 1, 1, "get_tokenApi")
    # content = """
    #             执行测试中……
    #             测试已完成！！
    #             生成报告中……
    #             报告已生成……
    #             报告已邮件发送！！
    #             """
    read = open(mail_path, encoding='utf-8')  # 打开需要发送的测试报告附件文件
    content = read.read()  # 读取测试报告文件中的内容
    read.close()
    mail.Body = content  # 将从报告中读取的内容，作为邮件正文中的内容
    mail.Send()
    print('Email sended successful!!!!')


if __name__ == '__main__':
    print(subject)
    outlook()
