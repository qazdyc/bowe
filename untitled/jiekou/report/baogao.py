from 实例.HTMLTestReportCN import HTMLTestRunner
import unittest
    #创建一个测试套件
def B_gao(name):
  suit = unittest.TestSuite()
    #将测试用六添加到测试套件里
    #将某一个类中所有的测试用例添加到测试套件中
    #第一个参数：存放测试脚本路径
    #第二个参数：匹配测试文中的通配符
    #自动去发现符合通配符的文件中以test开头的函数，提取出来放在dis列表中
  #"*_test.py"  name  suit
  for j in name:
   dis=unittest.defaultTestLoader.discover(r"C:\Users\dingxiaobai\PycharmProjects\untitled\jiekou\test",pattern="{}_test.py".format(j.strip()))
  for i in dis:
   suit.addTest(i)
  f=open("qaz2.html","wb")
  runner= HTMLTestRunner(
      stream=f,
      title="报告",
      description="报告名称",
      verbosity=2,
  )
  runner.run(suit)
  f.close()

# if __name__=='__main__':
#   B_gao()

