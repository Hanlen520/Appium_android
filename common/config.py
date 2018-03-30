#coding=utf-8

import  os




PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# the config of app
platformName = 'Android'
platformVersion= '5.1.1'
deviceName = '2d66b459'
app = PATH('./app/yymobile_client-7.5.2-SNAPSHOT-58674-official.apk')
appPackage = 'com.duowan.mobile'
appActivity= 'com.yy.mobile.ui.home.MainActivity'
