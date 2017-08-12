#!/usr/bin/env python
# encoding:utf-8
"""
功能：发送纯文本的邮件内容
演示：jupyter notebook 通过SMTP协议发送邮件
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
    from_addr = u"zelin_test@163.com"
    password = u"Zelin123456"  # 163设置的第三方授权码

    to_addr = u"zelin_test@163.com"
    smtp_server = u"smtp.163.com"

    msg = MIMEText(u'hello, sent by Python automation', 'plain', 'utf-8')
    msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
    msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print "sent ok"

if __name__ == "__main__":
    send_email()