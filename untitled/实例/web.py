#web自动化
#selenium：web自动化测试的工具集

#selenium1.0的组成
#1.selenium IDE 是火狐浏览器的一个插件
        #作用：录制和回放
#2.seleniun Grid 是自动化测试的一个辅助工具
        #作用：可以实现在不同的环境中执行测试
#3.selenium Rc selenium1.0是自动化测试的核心
           #作用：控制浏览器的行为

#selenium2.0的组成
#selenium1.0(selenium ide/grid/rc)
#   +
# webdriver   selenium2.0的核心
   #作用：控制浏览器的行为

#RC：通过将测试代码转换成JavaScript能够识别的动作，从而间接控制浏览器
#webdriver ：是通过将浏览器的所有的原生接口集成到webdriver驱动中，然后通过驱动直接控制浏览器


#定位一组对象
#层级定位：先定位一个大的区域,再从大的区域定位
#先定位父元素，再定位子元素
#
#
from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
dr = webdriver.Chrome()
#dr.get("https://www.ctrip.com")
dr.get("https://qzone.qq.com")
dr.maximize_window()
sleep(2)
# ww=dr.find_element_by_xpath('*[@id="J_cate"]/ul').find_element_by_tag_name("cate_menu_lk")
# print(len(ww))
# for i in ww:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(3)
dr.switch_to_frame("login_frame")
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="u"]').send_keys("1318740969")
sleep(2)
dr.find_element_by_xpath('//*[@id="p"]').send_keys("DY5997421QSAZ.")
sleep(2)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(2)
dr.switch_to_frame("tcaptcha_iframe")
sleep(2)
ww=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
#drag_and_drop两个参数(起始位置，结束位置)
#drag_and_drop_by_offset(函数有三个参数，起始位置，x轴坐标，y轴坐标)
sleep(5)
ActionChains(dr).drag_and_drop_by_offset(ww,140,0).perform()
# dr.find_element_by_xpath().send_keys()
# sleep(2)

