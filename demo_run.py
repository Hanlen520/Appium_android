#coding=utf-8

from appium import webdriver
from common import AppiumApi
from common.MakeCase import TestYY
import unittest
import  os
import time
import HTMLTestRunnerCN






if __name__ == '__main__':

    
    # os.system('StartAppium.bat') #启动appium服务
    time.sleep(3)
    
    suite = unittest.TestSuite()
    suite.addTest(TestYY('test_login'))
    filename = 'F:\\app.html'
    fb = file(filename, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fb, title='YYapptestreport', description='duowanAPP')
    runner.run(suite)
    fb.close()

    # os.system('CloseAppium.bat') #关闭appium服务
