from selenium import  webdriver
from time import sleep
# from selenium.webdriver.common.action_chains
#导入模块  智能等待
import selenium.webdriver.support.ui as ui
dr=webdriver.Chrome()
dr.get("https://www.baidu.com")
#sleep(2)#强制等待
#创建一个智能等待器
unit=ui.WebDriverWait(dr,10)
#如果定位的元素出现了就不必在等待
unit.until(lambda  dr:dr.find_element_by_link_text('hao123').is_displayed() )
#检测hao123这个文本内容是否出现，如果出现就执行下面的代码，如果没有出现就一直等待，最大等待10秒
dr.find_element_by_link_text('新闻').click()

# dr = webdriver.Chrome()
# dr.get("file:///C:/Users/dingxiaobai/Desktop/abc.html")
# sleep(2)
# dr.maximize_window()
# sleep(2)
#浏览器上下翻页
# for i in range(0,10000,500):
#     qq="var q=document.documentElement.scrollTop={}".format(i)
#     dr.execute_script(qq)
#     sleep(2)
#任何浏览器管理窗口的原理
#将每一个窗口用一个特定的字符来标识（句柄）
# #只需要获取到每一个窗口的标识号
#通过切换标识号，就能达到窗口的目的
#获取当前窗口的标识
# print(dr.current_window_handle)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# # dr.find_element_by_id("switcher_plogin").click()
# # while True:
# #  dr.find_element_by_name("wd").send_keys("极速体育")
# #  sleep(2)
# #  dr.find_element_by_id("su").click()
# #  sleep(2)
# #  dr.back()
# # back
# sleep(2)
# #获取所有已打开的窗口的标识号(是一个列表)
# aa=dr.window_handles
# #切换窗口
# dr.switch_to_window(aa[-1])
# print(dr.title)

# dr = webdriver.Chrome()
# dr.get("file:///C:/Users/dingxiaobai/Desktop/abc.html")
# sleep(2)
# dr.maximize_window()
# sleep(2)
# #处理弹出框
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(2)
# #切换到弹出框上去
# qq=dr.switch_to_alert()
# #1.获取弹出框上面的文本
# print(qq.text)
# #2.点击确定
# qq.accept()
# #3.点击取消
#qq.dismiss()
#4.向弹出框输入数据
#qq.send_keys("数据")
