#!/usr/bin/env python
# encoding:utf-8
"""
功能：发送HTML的邮件内容

演示：jupyter notebook 通过SMTP协议发送纯文本邮件
使用163邮箱作为测试：

用户名：zelin_test@163.com
密码：zelin123456
第三方授权码：Zelin123456
"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email():
    smtp_server = u"smtp.163.com"
    from_addr = u"zelin_test@163.com"
    password = u"woody123"  # 163设置的第三方授权码
    to_addr = u"zelin_test@163.com"
    test_res = u"test_result_2016-06-06 17-02-13.html"
    html_data = ''

    # fp = open(test_res, 'r')
    # data = fp.read()
    # fp.close()

    # with 语句
    with open(test_res) as fp:
        html_data = fp.read()  # 把文本内容一次性读入内存
    msg = MIMEText(html_data, 'html', 'utf-8')
    msg['From'] = _format_addr(u'自动化平台 <%s>' % from_addr)
    msg['To'] = _format_addr(u'开发人员 <%s>' % to_addr)
    msg['Subject'] = Header(u'【冒烟自动化】2017-08-19测试报告', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print "sent ok"

if __name__ == "__main__":
    send_email()