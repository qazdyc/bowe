from jiekou.config.dingdan import dingdan
from jiekou.data.duqu import shuju
import unittest
class D_dan(unittest.TestCase):
    ss=shuju()
    def test_1(self):
        aaa = dingdan().cha_mingxi(int(self.ss[1][2]))
        self.assertEqual(aaa["errMsg"], "处理成功")
    def test_2(self):
        aaa=dingdan().cha_mingxi(int(self.ss[1][2]))
        self.assertEqual("处理成功",aaa)

if __name__=='__main__':
  unittest.main()

  #自动的去检测继承了TestCase类的类中所有以est开头的类函数
  #将所有的以test开头的函数当成测试用例
  #执行顺序是按照test后的字符在ASCII中的先后顺序