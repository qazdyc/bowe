from 实例.HTMLTestReportCN import HTMLTestRunner
import  unittest
def report(test_name,report_path):
#第一步：创一个测试套件，理解成玩具枪
 suite =unittest.TestSuite()
#第二步：向测试套件里面添加测试用例，理解成向玩具枪弹夹里加子弹
 #suite.addTest("test_name")
 for i in test_name[0]:
    suite.addTet(i)
#第三步：将生成的测试结果写入html文件里，理解成玩具枪上挡
 with open(report_path,"wb") as fb:
      runner =HTMLTestRunner(
         stream=fb,
         title="报告名称",
         description="报告描述",
         verbosity=2,
         #输出内容的详细等级，默认是0，2代表最详细
     )
  #执行测试用例，并声称html测试报告，理解成玩具枪发射子弹
 runner.run(suite)

