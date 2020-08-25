# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import HTMLTestRunner111
import sys
# from asn1crypto._ffi import null
from twisted.python.test.deprecatedattributes import message
import os
reload(sys)
sys.setdefaultencoding( "utf-8" )

class HKautoCase02(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_h_k_load(self):
        u"""登录HKCRM系统"""
        driver = self.driver
        driver.get("http://172.17.24.77:8210/web-ngboss?")
        driver.find_element_by_id("STAFF_ID").click()
        driver.find_element_by_id("STAFF_ID").clear()
        driver.find_element_by_id("STAFF_ID").send_keys("91110029")
        driver.find_element_by_id("PASSWORD").click()
        driver.find_element_by_id("PASSWORD").clear()
        driver.find_element_by_id("PASSWORD").send_keys("123456")
        driver.find_element_by_id("loginBtn").click()
        time.sleep(2)
        #去掉系统提示弹窗
        driver.find_element_by_xpath('/html/body/div[9]/div[1]/div[2]/div/div/div[2]/button[1]').click()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        Jy=driver.find_element_by_xpath('//*[@id="welTab_tab_li_1"]').text
        print Jy
        if Jy==u"菜单地图":
            print u"系统登录成功"


    def test_load(self):
        #供后续方法复用
        driver = self.driver
        driver.get("http://172.17.24.75:8080/web-ngboss?")
        driver.find_element_by_id("STAFF_ID").click()
        driver.find_element_by_id("STAFF_ID").clear()
        driver.find_element_by_id("STAFF_ID").send_keys("91110029")
        driver.find_element_by_id("PASSWORD").click()
        driver.find_element_by_id("PASSWORD").clear()
        driver.find_element_by_id("PASSWORD").send_keys("123456")
        driver.find_element_by_id("loginBtn").click()
        time.sleep(2)
        #去掉系统提示弹窗
        driver.find_element_by_xpath('/html/body/div[9]/div[1]/div[2]/div/div/div[2]/button[1]').click()
        
    def test_PlanChange_Rule(self):
        u"""套餐变更-无服务号码登录"""
        driver = self.driver
        HKautoCase02.test_load(self)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="welTab_tab_li_1"]').click()
        time.sleep(3)
        driver.find_element_by_id("welTab_tab_li_1").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='停开机'])[1]/following::div[2]").click()
        driver.find_element_by_id("101501").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_115"]'))
        Jy000=driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]").text
        #print Jy000
        if Jy000[0:16]==u"请进行服务号码登录后再进行操作！":
            print u"服务号码登录前置规则校验成功"
        else:
            print u"服务号码登录前置规则校验失败"
            
    def test_VasDeal_Rule(self):
        u"""VAS受理-无服务号码登录"""
        driver = self.driver
        HKautoCase02.test_load(self)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="welTab_tab_li_1"]').click()
        time.sleep(3)
        driver.find_element_by_id("welTab_tab_li_1").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='停开机'])[1]/following::div[2]").click()
        driver.find_element_by_id("101502").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_115"]'))
        Jy001=driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]").text
        #print Jy000
        if Jy001[0:16]==u"请进行服务号码登录后再进行操作！":
            print u"服务号码登录前置规则校验成功"
        else:
            print u"服务号码登录前置规则校验失败"
        
    def test_ChangeSimCard(self):
        u"""补换卡-无服务号码登录"""
        driver = self.driver
        HKautoCase02.test_load(self)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="welTab_tab_li_1"]').click()
        time.sleep(3)
        driver.find_element_by_id("welTab_tab_li_1").click()
#         driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='销户'])[2]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='开台'])[1]/following::div[2]").click()
        driver.find_element_by_id("101403").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_115"]'))
        Jy002=driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]").text
        print Jy002[14:30]
        if Jy002[14:30]==u"请进行服务号码登陆后再进行操作！":
            print u"服务号码登录前置规则校验成功"
        else:
            print u"服务号码登录前置规则校验失败"
        
        
    def test_DestoryCus_Rule(self):
        u"""销户-无服务号码登录"""
        driver = self.driver
        HKautoCase02.test_load(self)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="welTab_tab_li_1"]').click()
        time.sleep(3)
        driver.find_element_by_id("welTab_tab_li_1").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='NGBOSS-TEST'])[1]/following::div[9]").click()
        driver.find_element_by_id("101102").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_115"]'))
        Jy003=driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]").text
        print Jy003[14:30]
        if Jy003[14:30]==u"请进行服务号码登陆后再进行操作！":
            print u"服务号码登录前置规则校验成功"
        else:
            print u"服务号码登录前置规则校验失败"
            
    def test_WLAN_Rule(self):
        u"""宽带移机-无服务号码登录"""
        driver = self.driver
        HKautoCase02.test_load(self)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="welTab_tab_li_1"]').click()
        time.sleep(3)
        driver.find_element_by_id("welTab_tab_li_1").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='资费变更'])[1]/following::div[2]").click()
        driver.find_element_by_id("101202").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_115"]'))
        Jy004=driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]").text
        print Jy004[0:14]
        if Jy004[0:14] == "用户没有登录或者登录已经失效 ":
            print u"服务号码登录前置规则校验成功"
        else:
            print u"服务号码登录前置规则校验失败"
            
        #对弹窗异常的处理    
#     def close_alert_and_get_its_text(self):
#         try:
#             alert = self.driver.switch_to_alert()
#             alert_text = alert.text
#             if self.accept_next_alert:
#                 alert.accept()
#             else:
#                 alert.dismiss()
#             return alert_text
#         finally: self.accept_next_alert = True
    
    def test_VAS_ydg(self):
        u"""VAS已订购列表查询"""
        driver = self.driver
        HKautoCase02.test_load(self)
        driver.find_element_by_id("NO_PASSWORD_LOGIN_CHECKBOX").click()
        driver.find_element_by_id("LOGIN_NUM").click()
        driver.find_element_by_id("LOGIN_NUM").clear()
        driver.find_element_by_id("LOGIN_NUM").send_keys("96630663")
        driver.find_element_by_id("LOGIN_BTN").click()
        time.sleep(3)
        #self.assertEqual(u"入参参数为空异常！", self.close_alert_and_get_its_text())
        #self.assertEqual(u"服务名称：bassi_IQueryOmMsgRecommendContentCSV_queryOmMsgRecommendContentQBO 调用服务bassi_IQueryOmMsgRecommendContentCSV_queryOmMsgRecommendContentQBO的业务代码发生异常", self.close_alert_and_get_its_text())
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='停开机'])[1]/following::div[2]").click()
        driver.find_element_by_id("101502").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_128"]'))
#         Jy005=driver.find_element_by_xpath('/html/body/div[1]/div/div[6]/ul/li[1]').text
#         /html/body/div[1]/div/div[6]/ul/li[2]
        
        for i in range(1,45):
#             XpathA='/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/table/tbody/tr{}'.format([int(i)])
            XpathA='/html/body/div[1]/div/div[6]/ul/li[]'.format([int(i)])
            #print XpathA
            Jy005=driver.find_element_by_xpath(XpathA).text
            print Jy005   
        
        
        
    def test_VAS_Query(self):
        u"""VAS受理查询组件"""
        driver = self.driver
        HKautoCase02.test_load(self)
        driver.find_element_by_id("NO_PASSWORD_LOGIN_CHECKBOX").click()
        driver.find_element_by_id("LOGIN_NUM").click()
        driver.find_element_by_id("LOGIN_NUM").clear()
        driver.find_element_by_id("LOGIN_NUM").send_keys("96630663")
        driver.find_element_by_id("LOGIN_BTN").click()
        time.sleep(3)
        #self.assertEqual(u"入参参数为空异常！", self.close_alert_and_get_its_text())
        #time.sleep(3)
        #self.assertEqual(u"服务名称：bassi_IQueryOmMsgRecommendContentCSV_queryOmMsgRecommendContentQBO 调用服务bassi_IQueryOmMsgRecommendContentCSV_queryOmMsgRecommendContentQBO的业务代码发生异常", self.close_alert_and_get_its_text())
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='停开机'])[1]/following::div[2]").click()
        driver.find_element_by_id("101502").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_128"]'))
        driver.find_element_by_xpath('//*[@id="insSearch"]').click()
        driver.find_element_by_xpath('//*[@id="insSearch"]').clear()
        driver.find_element_by_xpath('//*[@id="insSearch"]').send_keys('#SMS Package Intra 8')
        driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/span/button').click()
        time.sleep(5)
        Jy006=driver.find_element_by_xpath('/html/body/div[1]/div/div[6]/ul/li[1]').text
        if Jy006[0:20]=='#SMS Package Intra 8':
            print u"""查询组件功能校验成功"""
        else:
            print u"""查询组件功能校验失败"""
        
        
    def test_VAS_Add(self):
        u"""VAS订购页面"""
        driver = self.driver
        HKautoCase02.test_load(self)
        driver.find_element_by_id("NO_PASSWORD_LOGIN_CHECKBOX").click()
        driver.find_element_by_id("LOGIN_NUM").click()
        driver.find_element_by_id("LOGIN_NUM").clear()
        driver.find_element_by_id("LOGIN_NUM").send_keys("96630663")
        driver.find_element_by_id("LOGIN_BTN").click()
        time.sleep(3)
        self.assertEqual(u"入参参数为空异常！", self.close_alert_and_get_its_text(),'NOT SAME')
        self.assertEqual(u"服务名称：bassi_IQueryOmMsgRecommendContentCSV_queryOmMsgRecommendContentQBO 调用服务bassi_IQueryOmMsgRecommendContentCSV_queryOmMsgRecommendContentQBO的业务代码发生异常", self.close_alert_and_get_its_text())
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='停开机'])[1]/following::div[2]").click()
        driver.find_element_by_id("101502").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_128"]'))
        #进入订购页面
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/button').click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="offerFrame"]'))   
        Jy007=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/div/div/ul/li').text
        if Jy007==u"""vas受理二级目录""":
            print 'Go Add Success'
        else:
            print 'Go Add Default'
          
    def test_VAS_MessaQuery(self):
        u"""VAS目录查询组件功能校验"""
        driver = self.driver
        HKautoCase02.test_VAS_Add(self)
        driver.find_element_by_xpath('//*[@id="searchOfferkeyWord"]').click()
        driver.find_element_by_xpath('//*[@id="searchOfferkeyWord"]').clear()
        driver.find_element_by_xpath('//*[@id="searchOfferkeyWord"]').send_keys('#ISMS Pkg $19')
        time.sleep(3)
        Jy008=driver.find_element_by_xpath('//*[@id="offerId_200234"]').text
        if Jy008=='#ISMS Pkg $19':
            print 'Query Success'
        else:
            print 'Query Default'
        
    def test_upload(self):
        driver = self.driver
        HKautoCase02.test_load(self)
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        driver.find_element_by_id("menus_tab_li_1").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[2]").click()
        driver.find_element_by_id("10000220").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_115"]'))
        driver.find_element_by_id("busiNameValue_span").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='--请选择--'])[2]/following::div[1]").click()
        #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Upload'])[1]/following::span[3]").click()
        #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Upload'])[2]/following::input[2]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Upload'])[2]/following::input[2]").send_keys(u"D:\\工作\\导入文件\\SIM卡入库.txt")
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/ul/li[7]/div[2]/span/span[6]/form/input").send_keys(u"D:\\工作\\导入文件\\SIM卡入库.txt")
        time.sleep(500)
        print u"success！"
    
    
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
    testunit.addTest(HKautoCase02("test_h_k_load"))
    testunit.addTest(HKautoCase02("test_PlanChange_Rule"))
    testunit.addTest(HKautoCase02("test_VasDeal_Rule"))   
    testunit.addTest(HKautoCase02("test_ChangeSimCard"))   
    testunit.addTest(HKautoCase02("test_DestoryCus_Rule"))
    testunit.addTest(HKautoCase02("test_WLAN_Rule"))   
    testunit.addTest(HKautoCase02("test_VAS_ydg"))    
    testunit.addTest(HKautoCase02("test_VAS_Query"))
    testunit.addTest(HKautoCase02("test_VAS_Add"))    
    testunit.addTest(HKautoCase02("test_VAS_MessaQuery"))   
    testunit.addTest(HKautoCase02("test_upload"))
    
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  
    #打开一个文件，将result写入此file中
    fp=open("result"+now+".html",'wb')
    runner=HTMLTestRunner111.HTMLTestRunner(stream=fp,title='Test Report',description=u'南基五期香港新CRM自动化测试,test by taozhan')
    runner.run(testunit) 
    fp.close()