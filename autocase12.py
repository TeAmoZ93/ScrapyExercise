#-*- coding:utf-8 -*-
'''
Created on 2018年12月20日

@author: Administrator
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from autocase11 import autocase11yue
import autocase11
import HTMLTestRunner111
import cx_Oracle
from __builtin__ import int

class autocase12yue(autocase11.autocase11yue):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_DLLRule01(self):
        u"""大流量套餐副卡开户实名制校验"""
        driver = self.driver
        autocase11yue.test_FuWoHaoMaLoad(self,'13989010639')#调用已有的服务号码登录方法
        time.sleep(5)
        #driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        #driver.find_element_by_xpath('//*[@id="menu_ct"]')
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[1]/div/ul/li[2]/div[1]').click()
        #driver.find_element_by_xpath('//*[@id="menu_l1_ul"]/li[2]').click() 
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[4]/div/div[4]/ul/li[6]').click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_69"]'))
        #c_msg c_msg-full c_msg-h c_msg-error c_msg-phone-v
        time.sleep(1)
        ZLa=driver.find_element_by_xpath('//*[@class="content"]').text  
        #print ZLa      
#         array=[]
#         for c in ZLa:
#             array.append(c)
#         print array[1:11]
        #print ZLa[0:12]
        if ZLa[0:12] == "【1500000005】":
            print u"实名制规则校验成功"
        else:
            print u"实名制规则校验失败"
            
    def test_DLLRule02(self):
        u"""大流量套餐副卡开户一证五号校验"""
        driver = self.driver
        autocase11yue.test_FuWoHaoMaLoad(self,'18208014971')#调用已有的服务号码登录方法
        time.sleep(5)
        #driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[1]/div/ul/li[2]/div[1]').click()
        #driver.find_element_by_xpath('//*[@id="menu_l1_ul"]/li[2]').click() 
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[4]/div/div[4]/ul/li[6]').click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_69"]'))
        #c_msg c_msg-full c_msg-h c_msg-error c_msg-phone-v
        time.sleep(1)
        ZLb=driver.find_element_by_xpath('//*[@class="content"]').text 
        if ZLb[0:12]=="【1500000029】":
            print u"一证多名规则校验成功"
        else:
            print u"一证多名规则校验失败"
            
    def test_DLLRule03(self):
        u"""大流量套餐副卡开户欠费校验"""
        driver = self.driver
        autocase11yue.test_FuWoHaoMaLoad(self,'18308011766')#调用已有的服务号码登录方法
        time.sleep(5)
        #driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[1]/div/ul/li[2]/div[1]').click()
        #driver.find_element_by_xpath('//*[@id="menu_l1_ul"]/li[2]').click() 
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[4]/div/div[4]/ul/li[6]').click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_69"]'))
        #c_msg c_msg-full c_msg-h c_msg-error c_msg-phone-v
        time.sleep(1)
        ZLc=driver.find_element_by_xpath('//*[@class="content"]').text
        #print ZLc[0:18]
        if ZLc[0:18]=="【1500000005】 用户已欠费":
            print u"欠费规则校验成功"
        else:
            print u"欠费规则校验失败"
    
    def test_DLLRule04(self):
        u"""大流量套餐副卡开户证件类型校验"""
        driver = self.driver
        autocase11yue.test_FuWoHaoMaLoad(self,'14718919090')#调用已有的服务号码登录方法
        time.sleep(5)
        #driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[1]/div/ul/li[2]/div[1]').click()
        #driver.find_element_by_xpath('//*[@id="menu_l1_ul"]/li[2]').click() 
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[4]/div/div[4]/ul/li[6]').click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_69"]'))
        #c_msg c_msg-full c_msg-h c_msg-error c_msg-phone-v
        time.sleep(1)
        ZLd=driver.find_element_by_xpath('//*[@class="content"]').text
        #print ZLd[0:-7]
        if ZLd[0:-7]== u"CRMWEB_210000:号码是非身份证开户主卡,不允许办理副卡":
            print u"可办理证件类型规则校验成功"
        else:
            print u"可办理证件类型规则校验失败"
    
    def test_DLLRule05(self):
        u"""大流量套餐副卡可开户套餐校验"""
        driver = self.driver
        autocase11yue.test_FuWoHaoMaLoad(self,'17889115038')#调用已有的服务号码登录方法
        time.sleep(5)
        #driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[1]/div/ul/li[2]/div[1]').click()
        #driver.find_element_by_xpath('//*[@id="menu_l1_ul"]/li[2]').click() 
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[4]/div/div[4]/ul/li[6]').click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_69"]'))
        #c_msg c_msg-full c_msg-h c_msg-error c_msg-phone-v
        time.sleep(1)
        ZLe=driver.find_element_by_xpath('//*[@class="content"]').text
        print ZLe[0:-7]
        if ZLe[0:-7]== u"CRMWEB_210000:该主号没有在生效的国内大流量套餐！":
            print u"副卡开户套餐规则校验成功"
        else:
            print u"副卡开户套餐规则校验失败"
        #查询数据库可开户主套餐配置
        tns=cx_Oracle.makedsn('172.16.9.28',1522,'ng3cs') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql="select code_value from (SELECT t.*,t.rowid FROM base.bs_static_data t where t.code_type='UNLIMIT_QUANTITY_CONFIG_ORDER_TIMES')"
        c.execute(sql)
        rs=c.fetchall() 
        print rs
        c.close()
        conn.close()    
        
    def test_CustIdentity(self):
        u"""客户证件信息查询"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='权限管理'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='特殊客户名单管理'])[1]/following::li[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='手机号码'])[1]/preceding::div[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='证件类型：'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='--请选择--'])[2]/following::div[1]").click()
        driver.find_element_by_id("cond_GROUP_NAME").click()
        driver.find_element_by_id("cond_GROUP_NAME").clear()
        driver.find_element_by_id("cond_GROUP_NAME").send_keys("089167444080000000")
        driver.find_element_by_id("qryButton").click()
        time.sleep(3)
        exel=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[2]/table/thead/tr').text
        CustMesseage=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div/table/tbody/tr').text
        print exel
        print CustMesseage
        
    def test_YiZhengDduoMing(self):
        u"""一证多名查询"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='个人业务'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='免填单打印'])[2]/following::li[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("qryBox").click()
        driver.find_element_by_id("cond_IDEN_TYPE_CODE_span").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='--请选择--'])[2]/following::div[1]").click()
        driver.find_element_by_id("cond_IDEN_NR").click()
        driver.find_element_by_id("cond_IDEN_NR").clear()
        driver.find_element_by_id("cond_IDEN_NR").send_keys("430124199304118372")
        driver.find_element_by_id("qryButton").click()
        #time.sleep(900)
        datee=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[2]/table/thead/tr').text
        print datee
        #datee1=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/table/tbody/{}'.format(str(i))for i in range(1,6)).text
        for i in range(1,7):
            XpathA='/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/table/tbody/tr{}'.format([int(i)])
            #print XpathA
            datee1=driver.find_element_by_xpath(XpathA).text
            print datee1
    
    def test_AccountMessageChange(self):
        u"""账户资料变更"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='权限管理'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='个人'])[1]/following::li[1]").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("cond_SEARCH_VALUE").click()
        driver.find_element_by_id("cond_SEARCH_VALUE").clear()
        driver.find_element_by_id("cond_SEARCH_VALUE").send_keys("13638994528")
        #driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='查询值：'])[1]/following::button[1]").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[3]/button').click()
        time.sleep(30)
        #driver.find_element_by_xpath('//*[@id="acctPart"]').click()
        driver.find_element_by_id("acctinfo_ACCT_NAME").click()
        driver.find_element_by_id("acctinfo_ACCT_NAME").clear()
        driver.find_element_by_id("acctinfo_ACCT_NAME").send_keys(u"海阔天高")
        driver.find_element_by_id("submit").click()
        time.sleep(5)
        AccountMe=driver.find_element_by_xpath('/html/body/div[18]/div/div[2]/div[1]').text
        print AccountMe
        
    
    def test_SnMessageQuery(self):
        u"""白卡信息查询"""
        #查询出信息后，和数据库数据比对，输出比对结果
        #select * from res.res_empty_origin t where t.sn like '85180001080081969030';
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='客户管理'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='SIM卡管理'])[1]/following::li[1]").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("idle_SN_S").click()
        driver.find_element_by_id("idle_SN_S").clear()
        driver.find_element_by_id("idle_SN_S").send_keys("85180001080081969030")
        driver.find_element_by_id("idle_SN_E").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='重置'])[1]/following::button[1]").click()
        time.sleep(5)
        SnMessa=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div/table/tbody/tr').text
#         print SnMessa
#         print type(SnMessa)
        #查询数据库白卡的状态res_state
        tns=cx_Oracle.makedsn('172.16.9.28',1522,'ng3cs') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql="select res_state from (select * from res.res_empty_origin t where t.sn like '85180001080081969030')"
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close() 
        #比对前台信息&数据库状态  
        str = ''.join(rs[0])
        if SnMessa[22]==str[0]:
            print u"白卡信息查询功能无异常"
        else:
            print u"白卡信息查询功能异常"
            
    def test_editACCESSNUMBER(self):
        u"""号码生成"""
        #前置条件为先HLR信息管理生成号段，这部分查看autocase11yue.test_HLR_ADD方法
        #SELECT t.*,rowid FROM RES.RES_NUMSEG_HLR t where op_id='91110029' order by valid_date desc;
        driver = self.driver
        autocase11yue.load(self)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='客户管理'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='号码查询'])[1]/following::li[1]").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("edit_ACCESS_NUMBER_S").click()
        driver.find_element_by_id("edit_ACCESS_NUMBER_S").clear()
        driver.find_element_by_id("edit_ACCESS_NUMBER_S").send_keys("18809900011")
        driver.find_element_by_id("edit_NUM").click()
        driver.find_element_by_id("edit_NUM").clear()
        driver.find_element_by_id("edit_NUM").send_keys("1")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='结束号码'])[1]/following::div[1]").click()
        driver.find_element_by_id("instock").click()
        time.sleep(5)
        NumCreateMessa=driver.find_element_by_xpath('/html/body/div[16]/div/div[2]').text
        print NumCreateMessa
    
    def test_simEntry(self):
        u"""SIM卡入库"""
        #前置条件为先IMS与HLR信息管理生成IMS号段，这部分查看autocase11yue.test_IMS_HLR_ADD方法
        #SELECT t.*,rowid FROM RES.RES_IMSI_NUMSEG_REL t where op_id='91110029' order by valid_date desc;
        driver = self.driver
        autocase11yue.load(self)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='客户管理'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='SIM卡信息查询'])[1]/following::li[1]").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='资源类别：'])[1]/following::span[2]").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="frame_2e1b48d61b0891ebe7ec3e431bc9e666"]'))
        driver.find_element_by_name("RES_TYPE_TREE").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='资源规格：'])[1]/following::span[2]").click()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="frame_e5b9057dd81ca55ab7548d03ac45220d"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='【20023】4G-USIM卡'])[1]/following::input[1]").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("SPAN_MGMT_COUNTY").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="frame_af80ee05dd4623e5b750088f98d8ac90"]'))
        driver.find_element_by_name("DISTRICT_NAME").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("SPAN_STORE_ID").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="frame_af80ee05dd4623e5b750088f98d8ac90"]'))
        driver.find_element_by_name("STORE_NAME").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_name("REMARKS").click()
        driver.find_element_by_name("REMARKS").clear()
        driver.find_element_by_name("REMARKS").send_keys("AutoTest")
        driver.find_element_by_id("idle_USE_TYPE_span").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='--请选择--'])[3]/following::div[1]").click()
        driver.find_element_by_id("IMPORT_TYPE_span").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='IMSI ICC_ID PIN1 PIN2 PUK1 PUK2 KI OPC'])[1]/following::div[1]").click()
        time.sleep(3)
        #driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='文件1：'])[1]/following::span[5]").click()
        #driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='文件1：'])[1]/following::input[3]").clear() 
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='文件1：'])[1]/following::input[3]").send_keys(u"D:\\工作\\导入文件\\SIM卡入库.txt")
        time.sleep(3)
        driver.find_element_by_id("confirmButton").click()
        time.sleep(5)  
        errMessa=driver.find_element_by_xpath('/html/body/div[8]/div/div[2]').text
        print errMessa 
        
    def test_NumQuery(self):
        u"""号码查询"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='客户管理'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='号码管理'])[1]/following::li[1]").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("phone_ACCESS_NUMBER_S").click()
        driver.find_element_by_id("phone_ACCESS_NUMBER_S").clear()
        driver.find_element_by_id("phone_ACCESS_NUMBER_S").send_keys("18809900011")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='重置'])[1]/following::button[1]").click()
        time.sleep(10)
        NumMessa01=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div/table/tbody/tr').text
        print NumMessa01
      
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #unittest.main()#运行所有test开头的测试用例
    testunit=unittest.TestSuite()
    #将测试用例加入到测试容器中
#     testunit.addTest(autocase12yue("test_DLLRule01"))
#     testunit.addTest(autocase12yue("test_DLLRule02"))
#     testunit.addTest(autocase12yue("test_DLLRule03"))
#     testunit.addTest(autocase12yue("test_DLLRule04"))
#     testunit.addTest(autocase12yue("test_DLLRule05"))
#     testunit.addTest(autocase12yue("test_CustIdentity")) 
#     testunit.addTest(autocase12yue("test_YiZhengDduoMing"))  
#     testunit.addTest(autocase12yue("test_AccountMessageChange"))
#     testunit.addTest(autocase12yue("test_SnMessageQuery"))
#     testunit.addTest(autocase12yue("test_editACCESSNUMBER"))  
    testunit.addTest(autocase12yue("test_simEntry")) 
#     testunit.addTest(autocase12yue("test_NumQuery"))
    #获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    #打开一个文件，将result写入此file中
    fp=open("result"+now+".html",'wb')
    runner=HTMLTestRunner111.HTMLTestRunner(stream=fp,title='Test Report',description=u'南基五期新CRM个人业务自动化测试,test by taozhan')
    runner.run(testunit) 
    fp.close()
