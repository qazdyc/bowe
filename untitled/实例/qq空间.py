from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
dr = webdriver.Chrome()
dr.get("https://qzone.qq.com")
dr.maximize_window()
sleep(2)
dr.switch_to_frame("login_frame")
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="u"]').send_keys("1363747969")
sleep(5)
dr.find_element_by_xpath('//*[@id="p"]').send_keys("DYC1997421QAZ.")
sleep(5)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="aIcenter"]/span').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="fct_2212889395_311_0_1561104391_0_1"]/div[3]/div[1]/p/a[3]/i').click()
sleep(2)
for i in range(0,10000,500):
    qq="var q=document.documentElement.scrollTop={}".format(i)
    dr.execute_script(qq)
    sleep(5)
