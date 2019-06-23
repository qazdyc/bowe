#导入摸快
import unittest
from appium import webdriver
from time import sleep
from  diesheng.config import config_1
from  diesheng.config import config_2
#导入封装好的函数
#testCase 写测试用类，单元测试必须继承于unittest.TestSuite)
class DS(unittest.TestSuite):
#每个用例执行之前运行一次，作用：用于清理测试环境残留数据，初始化测试环境
    def setUp(self):#相当于init方法，类被调用的时候，会自动运行
       self.des = {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "emulator-5554",
            "appPackage": "com.qk.butterfly",
            "appActivity": ".main.LauncherActivity",
            "noReset": "true",

        }
        # http://127.0.0.1:4723/wd/hub固定的
        # 测试脚本与appium服务器建立一个session链接
       self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
    sleep(5.0)

#写测试用例的部分
def test_1(self):
     #使用脚本与测试数据相结合
 for i in config_1.read_data():
    #使用账号密码登录
    #self.dr.find_element_by_id("com.qk.butterfly:id/v_login_pwd").click()
    #进入账号密码登录界面
    self.dr.find_element_by_id("com.qk.butterfly:id/et_login_phone").send_keys("i[0]")
    self.dr.find_element_by_id("com.qk.butterfly:id/et_login_pwd").send_keys("i[1]")
    self.dr.find_element_by_id("com.qk.butterfly:id/tv_to_login").click()
    #断言
    sleep(5.0)
    #进入登录之后的页面
    #if else 处理登录成功与失败，也可使用try  except 语句做断言
    try:
        b=self.dr.find_element_by_id("com.qk.butterfly:id/tv_tab").text
        print("登录失败")
        self.assertequal(b,"登录",msg="登录失败")
    except:
          a = self.dr.find_element_by_id("com.qk.butterfly:id/tv_tab")[-1].text
          self.assertequal(a,"我的",msg="断言已登录成功")


#每个测试用例执行完之后，运行teardowm一次，作用：测试用例运行完，清理测试环境

def teraDown(self):
    self.dr.quit()
if __name__ == '__main__':
   # unittest.main()

    config_2.report(test_name=DS("test_1"),report_path="/Users/dingxiaobai/PycharmProjects/untitled/diesheng/data/d.html")