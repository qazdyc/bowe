# b=0
# a=int(input(">>>"))
# for i in range(2,a+1):
#     for j in range(2,i+1):
#         if i%j==0:
#             break
#     if i == j :
#         b+=j
# print(b)
#一百以内的质数之和



#一百以内的数相加
# a=1
# i=0
# while a<101:
#     i=a+i
#     a+=1
# print(i)

# import re
# a="vasv3q5jbj5b23j1233bkj2b675"
# b=re.compile("[0-9][0-9]+" )
# c=b.findall(a)
# print(len(c))
# from appium import webdriver
# from time import sleep
# des = {
#             "device": "android",
#             "platformName": "Android",
#             "platformVersion": "5.1.1",
#             "deviceName": "emulator-5554",
#             "appPackage": "com.qk.butterfly",
#             "appActivity": ".main.LauncherActivity",
#             "noReset": "true",
# }
# dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
# sleep(5)
# dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
# # s=dr.get_window_size()
# # x1=s['width'] * 0.5
# # y1=s['height'] * 0.7
# # y2=s['height'] * 0.25
# # while True:
# #     dr.swipe(x1,y1,x1,y2)
# #     sleep(15)



from appium import webdriver
from time import sleep
import unittest
from mr.config import cnnfig_2
class mr(unittest.TestCase):
    def setUp(self):
        self.des = {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "bc0d9588",
            "appPackage": "com.mooreshare.app",
            "appActivity": ".ui.activity.splash.SplashActivity",
            "noReset": "true",
        }
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(5)
    def test(self):
        self.dr.find_element_by_id('com.mooreshare.app:id/ll_title').click()
        sleep(2)
        try:
            a=self.dr.find_element_by_class_name('android.widget.RelativeLayout').find_element_by_class_name('android.widget.TextView').text
            self.assertEqual(a, "热门视频", msg="跳转成功")
            print('热门视频跳转成功')
        except:
            b= self.dr.find_element_by_id('com.mooreshare.app:id/rl_last_news').find_elements_by_class_name('android.widget.TextView')[0].text
            self.assertEqual(b,'即 时',msg='跳转失败')
            print('跳转失败')
        self.dr.find_element_by_id('com.mooreshare.app:id/rl_back').click()
        sleep(2)
        self.dr.find_element_by_id('com.mooreshare.app:id/ll_button_navi').find_elements_by_id('com.mooreshare.app:id/vg_button_navi')[2].click()
        sleep(2)
        try:
            c=self.dr.find_element_by_id('com.mooreshare.app:id/tv_bar_title').text
            self.assertEqual(c,'会议活动',msg='跳转成功')
            print('会议活动跳转成功')
        except:
            d= self.dr.find_element_by_id('com.mooreshare.app:id/rl_last_news').find_elements_by_class_name('android.widget.TextView')[0].text
            self.assertEqual(d,'即 时',msg='跳转失败')
            print('会议活动跳转失败')
        self.dr.find_element_by_id('com.mooreshare.app:id/rl_back').click()
        sleep(2)
        self.dr.find_element_by_id('com.mooreshare.app:id/ll_button_navi').find_elements_by_id('com.mooreshare.app:id/vg_button_navi')[1].click()
        sleep(2)
        try:
            c = self.dr.find_element_by_id('com.mooreshare.app:id/tv_bar_title').text
            self.assertEqual(c, '行业日报', msg='跳转成功')
            print('行业日报跳转成功')
        except:                                                                                                                          are.app:id/rl_last_news').find_elements_by_class_name(
                'android.widget.TextView')[0].text
            self.assertEqual(d, '即 时', msg='跳转失败')
            print('行业日报跳转失败')
        self.dr.find_element_by_id('com.mooreshare.app:id/rl_back').click()
        sleep(2)
        self.dr.find_element_by_id('com.mooreshare.app:id/ll_button_navi').find_elements_by_id('com.mooreshare.app:id/vg_button_navi')[3].click()
        sleep(2)
        try:
            c = self.dr.find_element_by_id('com.mooreshare.app:id/tv_bar_title').text
            self.assertEqual(c, '芯片设计', msg='跳转成功')
            print('芯片设计跳转成功')
        except:
            d = self.dr.find_element_by_id('com.mooreshare.app:id/rl_last_news').find_elements_by_class_name(
                'android.widget.TextView')[0].text
            self.assertEqual(d, '即 时', msg='跳转失败')
            print('行业日报跳转失败')
        self.dr.find_element_by_id('com.mooreshare.app:id/rl_back').click()
        sleep(2)
        self.dr.find_element_by_id('com.mooreshare.app:id/ll_button_navi').find_elements_by_id('com.mooreshare.app:id/vg_button_navi')[4].click()
        sleep(2)
        try:
            c = self.dr.find_element_by_id('com.mooreshare.app:id/tv_bar_title').text
            self.assertEqual(c, '专题报道(73)', msg='跳转成功')
            print('专题报道(73)跳转成功')
