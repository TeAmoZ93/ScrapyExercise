# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from HKautocase02 import HKautoCase02
import HTMLTestRunner111
import cx_Oracle
from sre_parse import Pattern
import re
from selenium.common.exceptions import NoSuchElementException#从selenium.common.exceptions 模块导入 NoSuchElementException类
"""
select access_num from (select access_num from ins1.um_subscriber_852 where subscriber_type=1 and 
subscriber_status=1 and rownum<100 order by dbms_random.value)  where rownum< 2;
"""
class HKautocase03(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_AccessLoad(self,access_num):
        #供后续复用
        u"""服务号码登录"""
        driver = self.driver
        driver.get("http://172.17.24.75:8085/web-ngboss")
        driver.find_element_by_id("STAFF_ID").click()
        driver.find_element_by_id("STAFF_ID").clear()
        driver.find_element_by_id("STAFF_ID").send_keys("P91110029")
        driver.find_element_by_id("PASSWORD").click()
        driver.find_element_by_id("PASSWORD").clear()
        driver.find_element_by_id("PASSWORD").send_keys("HKTest_#2019a")
        driver.find_element_by_id("loginBtn").click()
        time.sleep(3)
        #去掉系统提示弹窗
        driver.find_element_by_xpath('/html/body/div[9]/div[1]/div[2]/div/div/div[2]/button[1]').click()
        #driver.find_element_by_id("NO_PASSWORD_LOGIN_CHECKBOX").click()
        driver.find_element_by_id("LOGIN_NUM").click()
        driver.find_element_by_id("LOGIN_NUM").clear()
        driver.find_element_by_id("LOGIN_NUM").send_keys(access_num)
        driver.find_element_by_id("LOGIN_BTN").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[25]/div/div[2]/div[1]/div[2]/div/div[1]/input").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[25]/div/div[2]/div[2]/button[1]/span[1]").click()
        
        
    
    def test_VasAdd(self):
        u"""VAS订购"""
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql="select access_num from (select access_num from ins1.um_subscriber_852 where subscriber_type=1 and subscriber_status=1 and rownum<1000 order by dbms_random.value)  where rownum< 2"
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()    
        driver=self.driver
        y=rs[0]
        HKautocase03.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(2)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div/ul/li[6]/div[1]')
        time.sleep(2)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[2]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/button").click()
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="offerFrame"]'))
        driver.find_element_by_id("offerName_200234").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="iframe1"]'))
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/ul[3]/li[2]/div[2]/span/span/span[1]/span').click()
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[7]/button[3]').click()
        time.sleep(3)
        #driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div[7]/button[3]').click()
        driver.find_element_by_id("OFFER_BUTTON_SUBMIT").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]/button[2]').click()
        #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Close'])[1]/following::button[1]").click()
        time.sleep(10)
        SBwadeKuangJIA="wade_messagebox-(.*?)_ct"
        resA=driver.find_element_by_xpath('//*[starts-with(@id,SBwadeKuangJIA)]').text
        #order_idA=driver.find_element_by_xpath('//*[@id="wade_messagebox-d209225d1f681451139643f0e3029310_ct"]').text
        #print resA
        order_idA = re.search( r'\d{15}', resA).group(0)
        driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[2]/button').click()
        print order_idA
        time.sleep(10)#加延时确保后续取到订单号再查表
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql="select order_line_id,order_id,party_role_id,subscriber_ins_id,busi_item_code,access_num,valid_date,expire_date,data_status from ord.om_line_f_201903 t where t.order_id=%s" %order_idA
        #sql="select order_line_id,order_id,party_role_id,subscriber_ins_id,busi_item_code,access_num,valid_date,expire_date,data_status from ord.om_line_f_201903 t where t.order_id='"+order_idA+"'"
        c.execute(sql)
        rsA=c.fetchall() 
        print rsA
        c.close()
        conn.close()    
    
    def isElementPresent(self,by,value):
        u"""判断页面是否存在元素"""
        try:
            element = self.driver.find_element(by = by, value= value)
            #原文是except NoSuchElementException, e:
        except NoSuchElementException as e:
            #打印异常信息
            print(e)
            #发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:
            #没有发生异常，表示在页面中找到了该元素，返回True
            return True
        
    def test_VasDelete(self):
        u"""VAS退订"""
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql='''select access_num from (select access_num from ins1.um_subscriber_852 where subscriber_type=1 
        and subscriber_status=1 and rownum<1000 order by dbms_random.value)  where rownum< 2'''
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()    
        driver=self.driver
        y=rs[0]
        HKautocase03.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(2)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(2)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[2]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/ul/li[1]/div[4]").click()#删除
        time.sleep(3) 
        if self.isElementPresent('id','EDIT_EXP_DATE'):#手动录入时间场景
            driver.find_element_by_xpath('//*[@id="EDIT_EXP_DATE"]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="_Wade_DropDownCalendar_float"]/div[2]/div/div[7]/button[3]').click()
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[3]/div/button').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]/button[2]').click()
            time.sleep(10)
            SBwadeKuangJIA="wade_messagebox-(.*?)_ct"
            resB=driver.find_element_by_xpath('//*[starts-with(@id,SBwadeKuangJIA)]').text
            order_idB = re.search( r'\d{15}', resB).group(0)
            #driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div[2]/button').click()
            print order_idB
            time.sleep(10)#加延时确保后续取到订单号再查表
            tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
            conn=cx_Oracle.connect('aitest','aitest_1234',tns)
            c=conn.cursor()
            sql="select order_line_id,order_id,party_role_id,subscriber_ins_id,busi_item_code,access_num,valid_date,expire_date,data_status from ord.om_line_f_201903 t where t.order_id=%s" %order_idB
            c.execute(sql)
            rsA=c.fetchall() 
            print rsA
            c.close()
            conn.close()    
        else:#默认生效时间场景
            driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[3]/div/button').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]/button[2]').click()
            time.sleep(10)
            SBwadeKuangJIA="wade_messagebox-(.*?)_ct"
            resB=driver.find_element_by_xpath('//*[starts-with(@id,SBwadeKuangJIA)]').text
            order_idB = re.search( r'\d{15}', resB).group(0)
            #driver.find_element_by_xpath('/html/body/div[11]/div/div[2]/div[2]/button').click()
            print order_idB
            time.sleep(10)#加延时确保后续取到订单号再查表
            tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
            conn=cx_Oracle.connect('aitest','aitest_1234',tns)
            c=conn.cursor()
            sql="select order_line_id,order_id,party_role_id,subscriber_ins_id,busi_item_code,access_num,valid_date,expire_date,data_status from ord.om_line_f_201903 t where t.order_id=%s" %order_idB
            c.execute(sql)
            rsA=c.fetchall() 
            print rsA
            c.close()
            conn.close()   
    
    def test_VasQryDestory(self):
        u"""VAS受理销户用户校验"""
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql='select access_num from ins1.UM_SUBSCRIBER_852 where SUBSCRIBER_TYPE=1 and subscriber_status=4' 
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()    
        driver=self.driver
        y=rs[0]
        HKautocase03.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[2]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_129"]'))
        err1=driver.find_element_by_xpath('/html/body/div/div/div[2]').text
        print err1
        
        
        
    def test_VasQrySuspend(self):
        u"""VAS受理停机用户校验"""
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql='''select t.access_num from ins1.um_subscriber_852 t, ins1.um_prod_sta_852 m
            where t.subscriber_ins_id = m.subscriber_ins_id
            and t.data_status = '1'
            and t.subscriber_status = '1'
            and t.subscriber_type = '1'
            and m.prod_status = '2'
            '''
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()   
        driver=self.driver
        y=rs[0]
        HKautocase03.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[2]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        err2=driver.find_element_by_xpath('/html/body/div/div/div[2]').text
        print err2
        
    def test_VasQryCOrder(self):
        u"""VAS受理-变更在途工单校验"""
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql='''select access_num from ord.om_line where order_id in
         (select order_id from ord.om_order t where t.busi_code ='500140000002')
            '''
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()   
        driver=self.driver
        y=rs[0]
        HKautocase03.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[2]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        err3=driver.find_element_by_xpath('/html/body/div/div/div[2]').text
        print err3
        
    def test_ActiveDateQuery(self):
        u'''查客户激活时间'''
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql='''select access_num from ord.om_line where order_id in
         (select order_id from ord.om_order t where t.busi_code ='500220000005')
            '''
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()   
        driver=self.driver
        y=rs[2]
        HKautocase03.test_AccessLoad(self,y)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="myMoblie"]').click()
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_136"]'))
        time.sleep(1)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="baseFrame"]'))
        goal=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/ul/li[17]').text
        
        print goal
         
         
    def test_VasQryNOrder(self):
        u"""VAS受理-客户资料变更在途工单校验"""
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql='''select access_num from ord.om_line where order_id in
         (select order_id from ord.om_order t where t.busi_code ='500220000005')
            '''
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()   
        driver=self.driver
        y=rs[2]
        HKautocase03.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[2]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        time.sleep(5)
        #//*[@id="insSearch"]
        if self.isElementPresent('id','insSearch'):
            print u"校验成功！"
        else:
            print u"校验失败"
            
    
    def test_VasQryNactive(self):
        u"""VAS受理-开户未激活用户校验"""
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql="select access_num from ins1.UM_SUBSCRIBER_852 where SUBSCRIBER_TYPE=1 and subscriber_status=10"
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()   
        driver=self.driver
        y=rs[0]
        time.sleep(5)
        HKautocase03.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[2]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_128"]'))
        time.sleep(5)
        #//*[@id="insSearch"]
        if self.isElementPresent('id','insSearch'):
            print u"校验成功！"
        else:
            print u"校验失败"
            
    def test_VasChange(self):
        u"""VAS特征值变更"""  
        driver=self.driver
        HKautocase03.test_AccessLoad(self,'93157018')
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[2]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        driver.find_element_by_xpath('//*[@id="200021_insLi"]').click()
        time.sleep(5) 
#         js="document.getElementById('Part_152852000032').style.display='block';"
#         driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="chaSpec_152852000032"]').send_keys("333")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="OFFER_BUTTON_CHANGE"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="myDialog"]/div/div[3]/div[1]/button[2]').click()
        time.sleep(10)
        SBwadeKuangJIA="wade_messagebox-(.*?)_ct"
        resB=driver.find_element_by_xpath('//*[starts-with(@id,SBwadeKuangJIA)]').text
        order_idB = re.search( r'\d{15}', resB).group(0)
        #driver.find_element_by_xpath('/html/body/div[11]/div/div[2]/div[2]/button').click()
        print order_idB
        time.sleep(10)#加延时确保后续取到订单号再查表
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst')       
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql="select order_line_id,order_id,party_role_id,subscriber_ins_id,busi_item_code,access_num,valid_date,expire_date,data_status from ord.om_line_f_201903 t where t.order_id=%s" %order_idB
        c.execute(sql)
        rsA=c.fetchall() 
        print rsA
        c.close()
        conn.close()   
        

    def test_VasTimeIsNull(self):
        u"""VAS受理-订购生效时间非空校验"""
        driver=self.driver
        HKautocase03.test_AccessLoad(self,"52223104")
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[2]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/button').click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="offerFrame"]'))
        driver.find_element_by_id("offerName_200234").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="iframe1"]'))
        time.sleep(3)
        driver.find_element_by_id("OFFER_BUTTON_SUBMIT").click()
        time.sleep(3)
        IsNullMessa=driver.find_element_by_xpath('//*[@id="wade_tipbox-1_content"]').text
        print IsNullMessa
        

    def test_VasSpecIsNull(self):
        u"""VAS受理-订购特征值非空校验"""
        driver=self.driver
        HKautocase03.test_AccessLoad(self,"52223104")
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[2]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/button').click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="offerFrame"]'))
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="searchOfferkeyWord"]').send_keys("KID")
        driver.find_element_by_xpath('//*[@id="searchOffersearchButton"]').click()
        time.sleep(3)
        driver.find_element_by_id("offerName_200844").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="iframe1"]'))
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/ul[3]/li[2]/div[2]/span/span/span[1]/span').click()
        driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div[7]/button[3]').click()
        time.sleep(1)
        driver.find_element_by_id("OFFER_BUTTON_SUBMIT").click()
        time.sleep(3)
        IsNullMessa=driver.find_element_by_xpath('html/body/div[10]/div/div[2]/div/div[2]').text
        print IsNullMessa
        
    def test_VasHC(self):
        u"""VAS受理-互斥订购"""
        driver=self.driver
        HKautocase03.test_AccessLoad(self,"52223104")
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[2]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/button').click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="offerFrame"]'))
        time.sleep(3)
        driver.find_element_by_id("searchOfferkeyWord").click()
        driver.find_element_by_id("searchOfferkeyWord").click()
        driver.find_element_by_id("searchOfferkeyWord").clear()
        driver.find_element_by_id("searchOfferkeyWord").send_keys("200792")
        driver.find_element_by_xpath('//*[@id="searchOffersearchButton"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="offerId_200792"]').click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="iframe1"]'))
        driver.find_element_by_xpath('//*[@id="OFFER_BUTTON_SUBMIT"]').click()
        time.sleep(2)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/button').click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="offerFrame"]'))
        time.sleep(3)
        driver.find_element_by_id("searchOfferkeyWord").click()
        driver.find_element_by_id("searchOfferkeyWord").click()
        driver.find_element_by_id("searchOfferkeyWord").clear()  
        driver.find_element_by_id("searchOfferkeyWord").send_keys("200348")
        driver.find_element_by_xpath('//*[@id="searchOffersearchButton"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="offerId_200348"]').click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="iframe2"]'))
        driver.find_element_by_xpath('//*[@id="chaSpec_52223104_152852000017"]').send_keys('888')
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/ul[3]/li[2]/div[2]/span/span/span[1]').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[7]/button[3]').click()
        driver.find_element_by_xpath('//*[@id="OFFER_BUTTON_SUBMIT"]').click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        driver.find_element_by_xpath('/html/body/div[2]/div[1]').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]/button[2]').click()
        time.sleep(5)
        HC=driver.find_element_by_xpath('html/body/div[8]/div/div[2]/div/div[2]').text
        print HC
        
        
    
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
#     testunit.addTest(HKautocase03('test_VasChange'))
#     testunit.addTest(HKautocase03('test_VasQryDestory'))
#     testunit.addTest(HKautocase03("test_VasDelete"))
#     testunit.addTest(HKautocase03("test_VasAdd"))  
#     testunit.addTest(HKautocase03('test_VasQrySuspend'))
#     testunit.addTest(HKautocase03('test_VasQryCOrder'))
#     testunit.addTest(HKautocase03('test_VasQryNOrder'))
#     testunit.addTest(HKautocase03('test_VasSpecIsNull'))
#     testunit.addTest(HKautocase03('test_VasTimeIsNull'))
#     testunit.addTest(HKautocase03('test_VasHC'))
#     testunit.addTest(HKautocase03('test_VasQryNactive'))
    testunit.addTest(HKautocase03('test_ActiveDateQuery'))


    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  
    #打开一个文件，将result写入此file中
    fp=open("result"+now+".html",'wb')
    runner=HTMLTestRunner111.HTMLTestRunner(stream=fp,title='Test Report',description=u'南基五期香港新CRM自动化测试,test by taozhan')
    runner.run(testunit) 
    fp.close()