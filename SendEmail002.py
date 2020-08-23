#-*- coding=utf-8 -*-
'''
Created on 2020年7月23日
@author: Administrator
'''

import time 
import smtplib
import schedule
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def qqEmail():
    #连接邮箱服务器&登陆
    qqEmailServer=smtplib.SMTP_SSL('smtp.qq.com',465)
    password=open('password.txt','r+').read()
    account = '1001@qq.com'
    receiver=('xxy@163.com')
    qqEmailServer.login(account, password)
    #构建抬头主题部分内容
    msg1=MIMEMultipart()
    msg1['from']='1001@qq.com<1001@qq.com>'
    msg1['To']='xxy@163.com<xxy@163.com>'
    subject = input('请输入你的邮件主题：')
    msg1['Subject']=Header(subject, 'utf-8')
    #构建邮件内容
    content=input('请输入邮件正文：')
    message = MIMEText(content, 'plain', 'utf-8')
    msg1.attach(message)
    #构造附件
    SendFile=open('500.html','rb').read()
    att=MIMEText(SendFile,'base64','UTF-8')
    att["Content-Disposition"]='attachment;filename="500.html"'
    msg1.attach(att)
    #附件图片邮件正文直接展示
    image_data=open('QQ图片20200819203809.png','rb').read()
    image=MIMEImage(image_data)
    image.add_header('Content-ID', '<image>')
    msg1.attach(image)
    content='''
    <p>图片附件，直接展示在邮件文本区域</p>
    <img src="cid:image">
    '''
    html=MIMEText(content,'html','utf-8')
    msg1.attach(html)
       
    try:
        qqEmailServer.sendmail(account, receiver,msg1.as_string())
        print ('邮件发送成功')
    except smtplib.SMTPDataError as e:
        print ('邮件发送失败:%s'%e)    
    qqEmailServer.quit()
    
if __name__=='__main__':
    qqEmail()
    '''
#     Email163()
    schedule.every(2).seconds.do(qqEmail)        #每2s执行一次job()函数
#     schedule.every(10).minutes.do(qqEmail)       #部署每10分钟执行一次job()函数的任务
#     schedule.every().hour.do(qqEmail)            #部署每×小时执行一次job()函数的任务
#     schedule.every().day.at("10:30").do(qqEmail) #部署在每天的10:30执行job()函数的任务
#     schedule.every().monday.do(qqEmail)          #部署每个星期一执行job()函数的任务
#     schedule.every().wednesday.at("13:15").do(qqEmail)#部署每周三的13：15执行函数的任务
    while True:
        schedule.run_pending()
        time.sleep(1)
    '''

