#unittest 单元测试模块
#生成html测试报告
from 实例 import HTMLTestReportCN
#用于单元测试，验证预期与实际结果是否一致，一直代表通过，不一致代表失败
import unittest
#TestCase:代表测试用例
class T(unittest.TestCase):
    #测试用例方法，必须以test
   def test_1(self):
       #预期结果
       x="宝马"
       #实际结果
       y="劳斯莱斯"
       #第一个断言方法，判断预期结果与实际结果是否相等
       #x,y位置是可以互换
       self.addTypeEqualityFunc(x, y, msg="msg的作用就是填写备注信息")

   def test_2(self):
        # 预期结果
        x = "宝马"
        # 实际结果
        y = "宝马"
        # 第一个断言方法，判断预期结果与实际结果是否相等
        # x,y位置是可以互换
        self.addTypeEqualityFunc(x, y, msg="msg的作用就是填写备注信息")
if __name__ == '__main__':
#使用unittest类的main方法，自动加载当前脚本中的类，并自动运行测试用例
  #unittest.main()

  #############生成测试报告################
 #第一步：创一个测试套件，理解成玩具枪
 suite = unittest.TestSuite()
#第二步：向测试套件里面添加测试用例，理解成向玩具枪弹夹里加子弹
 suite.addTest(T("test_1"))
 suite.addTest(T("test_2"))
#第三步：将生成的测试结果写入html文件里，理解成玩具枪上挡
 with open("a.html","wb") as fb:
  runner = HTMLTestReportCN.HTMLTestRunner(
         stream=fb,
         title="报告名称",
         description="报告描述",
         verbosity=2,
         #输出内容的详细等级，默认是0，2代表最详细
     )
  #执行测试用例，并声称html测试报告，理解成玩具枪发射子弹
  runner.run(suite)

