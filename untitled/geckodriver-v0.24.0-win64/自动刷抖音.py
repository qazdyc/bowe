from appium import webdriver
from time import sleep
des = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "emulator-5554",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": ".main.MainActivity",
}
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
sleep(5)
s=dr.get_window_size()
x1=s['width'] * 0.5
y1=s['height'] * 0.7
y2=s['height'] * 0.25
while True:
    dr.swipe(x1,y1,x1,y2)
    sleep(15)
