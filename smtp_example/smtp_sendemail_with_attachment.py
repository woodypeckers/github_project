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
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


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

    # 邮件对象:
    msg = MIMEMultipart()
    msg['From'] = _format_addr(u'自动化平台 <%s>' % from_addr)
    msg['To'] = _format_addr(u'开发人员 <%s>' % to_addr)
    msg['Subject'] = Header(u'【冒烟自动化】2016-06-06测试报告', 'utf-8').encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText(u'详情请看附件...', 'plain', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个html文件:
    with open(test_res, 'rb') as f:
        # 设置附件的MIME和文件名，这里是html类型:
        mime = MIMEBase('html', 'html', filename=test_res)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=test_res)
        mime.add_header('Content-ID', '<0>')  #cid=0
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    server = smtplib.SMTP(smtp_server)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print "sent ok"

if __name__ == "__main__":
    send_email()