from appium import webdriver
from time import sleep
#建立与appium服务器需要的参数，以字典形式
des = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "emulator-5554",
  "appPackage": "com.tencent.tim",
  "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
  "noReset": "true"
}
#http://127.0.0.1:4723/wd/hub固定的
#测试脚本与appium服务器建立一个session链接
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
sleep(2)
#滑动
#第一步先获取屏幕大小
#s=dr.get_window_size()
#第二步放缩x,y轴
#x1 = s["width"] * 0.5
#y1 = s["height"] * 0.25
#y2 = s["height"] * 0.75
#第三步使用swipe方法进行滑动操作
#dr.swipe(x1,y1,x1,y2)
#sleep(10)
#dr.quit()
#安卓独有的定位
#输入账号
#先清空输入框，在输入
dr.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱").clear()
dr.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱").send_keys("1363747969")
#输入密码
dr.find_element_by_id("com.tencent.tim:id/password").send_keys("DYC1997421QAZ.")
#点击登录
dr.find_element_by_id("com.tencent.tim:id/login").click()
#dr.find_element_by_id("com.tencent.tim:id/login").click()
#第一步点击办公
dr.find_element_by_id("com.tencent.tim:id/tabs").find_element_by_class_name()
#第二步点击好友动态
t=dr.find_element_by_id("com.tencent.tim:id/lebasv").find_element_by_class_name()
t[-1].click()
sleep(0.5)
#第三步点赞
x=dr.find_element_by_class_name("android.widget.ImageView")
print(x)
x[1].click()
sleep(2)
x[2].click()
#层级定位
#第一步，先定义一个唯一的元素
#第二步，在定位多个相同元素
#a=dr.find_element_by_id('com.ss.android.ugc.aweme:id/ca9').find_element_by_class_name('android.widget.FrameLayout')
# print(a)
# for i in a:
#  sleep(0.5)
#  i.click()
#  sleep(0.5)
 #退出app并关闭
dr.quit()

