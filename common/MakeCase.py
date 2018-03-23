#coding=utf-8

import time
import unittest
from appium import webdriver


class TestYY(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '2d66b459'
        # desired_caps['app'] = PATH('yymobile_client-7.5.2-SNAPSHOT-58674-official')
        desired_caps['appPackage'] = 'com.duowan.mobile'
        desired_caps['appActivity'] = 'com.yy.mobile.ui.home.MainActivity'
        # 如果设置的是app包的路径，则不需要配appPackage和appActivity
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(6)


    
    def test_login(self):        
        
        el=self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("个人中心")')
        el.click()

        time.sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("登录YY")').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.yy.mobile.plugin.main:id/btn_login').click()   # 点击登录头像按钮，进行登录，跳转到登录界面
        time.sleep(2)
        
        self.driver.find_element_by_id('com.yy.mobile.plugin.main:id/EdtAccount').send_keys('13524352709')# 输入用户名
        self.driver.find_element_by_id('com.yy.mobile.plugin.main:id/EdtPassword').send_keys('chx175246')# 输入密码
        
        
        name = self.driver.find_element_by_id('com.yy.mobile.plugin.main:id/tv_user_name').text

        # 添加断言，若昵称不正确，则打印错误信息
        try:
            assert 'chqtest2' in name
            print 'loginUser is right'
        except AssertionError as e:
            print 'loginUser is Error'
            
        self.driver.find_element_by_id('com.yy.mobile.plugin.main:id/iv_setting').click()# 点击设置按钮，进入设置页面
        time.sleep(2)
        
        AppiumApi.swipeUp(self.driver, n=2)
        time.sleep(2)

        self.driver.find_element_by_id('com.yy.mobile.plugin.main:id/tv_logout').click()# 点击退出登录
        self.driver.find_element_by_id('com.duowan.mobile:id/cs').click()# 点击确定
        time.sleep(2)
        
       
     
    def tearDown(self):
        self.driver.quit()
