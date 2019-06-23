import unittest
from appium import webdriver
from time import sleep
from  wenjian.config import config_2
import warnings
class DS(unittest.TestCase):

    # 每个用例执行之前运行一次，作用：用于清理测试环境残留数据，初始化测试环境
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.des = {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "emulator-5554",
            "appPackage": "com.qk.butterfly",
            "appActivity": ".main.LauncherActivity",
            "noReset": "true",
        }
        # http://127.0.0.1:4723/wd/hub 固定的，写死localhost==127.0.0.1
        # 测试脚本与appium服务器建立一个session连接
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(5.0)

    # 写测试用例的部分
    def text(self):
        sleep(2)
        # 使用账号密码登录蝶声
        # 点击密码，进入手机号、密码登录页面
        self.dr.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱").clear()
        # 进入账号密码登录页面之后
         self.dr.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱").send_keys("1363747969")
         self.dr.find_element_by_id("com.tencent.tim:id/password").send_keys("DYC1997421QAZ.")
         self.dr.find_element_by_id("com.tencent.tim:id/login").click()

        # 断言
        sleep(5.0)
        # 进入登录之后的页面
        a = self.dr.find_elements_by_id('com.qk.butterfly:id/tv_tab')[-1].text
        self.assertEqual(a, '我的',msg="断言已经登录成功")

    # # 每个测试用例执行完毕之后，运行teardown一次，作用：测试用例运行完，清理测试环境



    def tearDown(self):
        self.dr.quit()
if __name__ == '__main__':
    unittest.main()
    config_2.report(test_name=DS("test_1"),report_path="/Users/dingxiaobai/PycharmProjects/untitled/wenjian/data/d.html")



