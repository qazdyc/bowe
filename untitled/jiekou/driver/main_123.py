#driver中主要是控制回归测试时只跑那些模块儿的用例
from jiekou.report.baogao import B_gao
with open("a.txt","r")as f:
    a=f.readlines()
    if "all" in a:
        B_gao("*")
    else:
        B_gao(a)