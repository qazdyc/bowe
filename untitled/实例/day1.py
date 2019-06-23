#a=["abc","defg","abcdefg","abcdegf"]
#print (a[::3])
#b= a.upper()
#print(b)
#c= "-".join(a)
#print(c)
#a ="user{sex}ss{name}sa{nihao}"
##print(b)
#a ="helo%s,你好我今年%d岁"
#b = a % ("baibai",99 )
#print(b )
#a="agdagdagahty"
#print(len(a) )
#bowen = [2,4,5,1,2,3,8,6,54,]
#bowen.append("你好")
#bowen .remove(100)
#bowen.insert(4,"你好")
#bowen.sort()
# bowen.reverse()
# bowen.count(2)
# bowen.pop(1)
#bowen[0]=1997
#a=[1,3,4,5]
# import copy
# b=[5,23,7,8]
# c=[8,54,7,b,100]
# #a.extend(b)
# dd=copy.deepcopy(c)
# b.append(456)
# #c.append(987)
# #dd=c.copy()
# print(c)
# print (dd)
#a=(2,3,1,4,6,8,9)
#print(type(a))
#a = {"name":"啊明","age":"23"}
#print(type(a))
#a["sex"]="nan"
#print(a)
#a.pop("age")
#print(a)
#a.popitem()
#b=a.keys()
#c=a.values()
#c=a.items()
#print(a)
# a={12,54,65,43,"sa"}
# b={43,54,23,876}
# #a.remove(65)
# #a.pop()
# #a.update(b)
# #print(a|b)
# # print(a&b)
# c=(b-a)
# print(type(c))
# a=input(">>>")
# a=int(a)
# if a >= 90 :
#  print("优")
# elif a >=80 and a <=90:
#     print("良")
# elif a >=70 and a <=80:
#     print("及格")
# print("不及格")
# a=input("请输入")
# a=int(a)
# if a % 2==0:
#  if a%3==0:
#       print("hello world")
#  else:
#        print("hello")
# elif a%3==0:
#      print("world")
# else:
#     print("123")
#
#a=[21,534,421,421,4,3]
# a=0
# for i in range(1,101,1):
#     a=a+i
#     print(a)
#
# for i in range(3):
#     print("大循环")
#     for j in range(3):
#       print("小循环")

# for i in  range(10):
#     if i>7:
#         break
#     print(i)
#

# import  random
# a= random.randrange(1,10)
# for i in  range(1,4):
#     b = input(">>>")
#     b = int(b)
#     if  a < b :
#         print("大了大了,还有{}次机会".format(3-i))
#     elif a > b :
#         print("小了小了,还有{}次机会".format(3-i))
#     else:
#         print("恭喜答对了")
# else :
#      print("菜")
#
#
# for i in range(1,10):
#     for j in range(1,10):
#        if i < j+1:
#            print("{}*{}={}".format(i,j,i*j),end="\t")
#     print("")
#
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     d=a**3+b**3+c**3
#     if d==i:
#         print(i)
#
# a=[40,20,20,80,20]
# #b =a.count(20)
# a.remove(40)
# #a=input(">>")
# print(a)
# a=input("请输入数字")
# a=list(a)
# a.reverse()
# #if a[3]==a[-3]:
# print(a)
#
# a=5
# while a<10:
#     print("nihao")
#     a += 1
# a=1
# i=0
# while a < 101:
#     i=i+a
#     a=a+1
# print(i)
# a+=1
# a=[]
# while True:
#   a = input("请输入成绩")
#   a=a.split(",")
#   for i,j in enumerate(a):
#     a[i]=int(j)
#   b=sum(a)//len(a)
#   if a[0]< 0:
#       break
#   print("平均数{}".format(b))
#   for k in a:
#         if k < b:
#          print("低于平均数为{}".format(k))
#
#b=[i**2 for i in range(6) if i > 3]
#print(b)
# while True:
#     a=input(">>>")
#     a=a.split(",")
#     a=[int(i) for i in a]
#     b=sum(a)/len(a)
#     if a[0] < 0:
#         break
#     print("低于平均数为{}".format(a))
#     c = [k for k in a if k < b ]
#     print(c)
# a = [12,12,78,12,12,45,78,45,78]
# for i in a:
#     b = a.count(i)
#     if b > 1:
#         for j in range(b-1):
#             a.remove(i)
# print(a)
#
#f=open(r"a.txt","w",encoding="utf_8")
# for i in range(1, 10):
#   for j in range(1,i+1):
#     f.write("{}*{}={}\t".format(j,i,i*j))
#   f.write("\n")
# b=f.readline()
# d=f.readline()
# q=f.readline()
# print(b,d,q)
#f.close()
 #for i in range(21):
# j=1
# # x=14
# # z=17
# f=open(r"a.txt","r",encoding="utf_8")
# #for i,j in enumerate(f.readlines()):
# for i in f.readlines():
#  print('第%d行内容:%s;长度:%d' % (j,i,len(i)))
#  j=j+1
# #    if i >= x+1 :
# #        if i <= z:
# print(j)
# f.close()
# a=input("请输入数字")
# b=a.split(",")
# c=len(b)
# for i in  range(c):
#     for j in  range(c-1):
#         if int(b[j]) > int(b[j+1]):
#             t=b[j]
#             b[j]=b[j+1]
#             b[j+1]=t
# print(b)

# f=open(r"a1.txt","w",encoding="utf_8")
# f.close()
#
# a=[12,45,67,94,12,35,80]
# a.sort()
# b=len(a)
# for i,j in enumerate(a):
#     if b - i < 3:
#      print (i,j)
# f =open(r"C:\Users\dingxiaobai\Desktop\timg.jpg", "rb")
# b =f.read()
# ff= open(r"C:\Use"r"rs\dingxiaobai\Desktop\timg2.jpg", "wb")
# ff.write(b)
# f.close()
# a="123"
# c=0
# for i,j in enumerate(a):
#     for k in range(10):
#         if str(k) == j:
#             c+=k*10**(len(a)-1-i)
# print(c)
# a=0
#
# def asd(c):
#     a=0
#     for i in  range(1,c+1):
#       a+=i
#     return c
# for i in  range(10,41,10):
#     e=asd(i)+2
#     print(e)
# # asd(10,12)+2
# # #print(w)
# def asd(c,v,d):
#    a=0
#    if d=="+":
#        a=c+v
#    if d=="-":
#        a=c-v
#    if d=="*":
#        a=c*v
#    if d=="/":
#        a==c/v
#    return a
# e=asd(2,10,"-")
# print(e)
# a=lambda r,f : r + f
# q=lambda r,f : r * f
# z=lambda r,f : r / f
# e=lambda r,f : r - f
# while True:
#     s =input("..")
#     if "-" in s:
#          p=s.split("-")
#          print(e(int(p[0]),int(p[1])))
#     elif "+" in s:
#          p=s.split("+")
#          print(a(int(p[0]),int(p[1])))
#     elif "/" in s:
#          p=s.split("/")
#          print(z(int(p[0]),int(p[1])))
#     elif  "*"in s:
#          p=s.split("*")
#          print(q(int(p[0]),int(p[1])))
#     else:
#      break
# def asd(z,x,c):
#     z=list(z)
# for i in range(x,d) :
#   f = list(z)
#   b = int(x), int(c)
#     print(i,j)
# # for  m in range(3):
# #      m.pop(2)
#
# asd("dingyuhcang",2,4)
#
#十进制转十六进制
# a=int(input(">>>"))
# ff = [str(i) for i in  range(10)] + ["a","b","c","d","e","f"]
# q=""
# while True:
#     b= a % 16
#     q=q + ff[b]
#     a= a // 16
#     if a==0:
#         break
# print(q[::-1])
# goods=[
#     {"name":"电脑","price":1999},
#     {"name":"鼠标","price":10},
#     {"name":"游艇","price":20},
#     {"name":"美女","price":998},
# ]
# guc_list=[]
# z=input("钱包余额：")
# z=int(z)
# while True:
#   goods = list(goods)
#   for index,i in enumerate(goods):
#     print(index + 1,i)
#   b=input("请输入商品号添加至购物车：")
#   b=int(b)
#   if b <= len(goods) and b > 0:
#       print("你要购买的是：",goods[b - 1][0])
#       if z >= goods[b - 1][1]:
#           guc_list.append(goods[b - 1][0])
#           z -= goods[b - 1][1]
#           print("你以购买了"+goods[b - 1][0])
#       else:
#           print("余额不足")
#           print("当前购买的产品")
#           for t in guc_list:
#               print("当前余额",z)
#               exit()
#   else:
#       print("")


# a=input(">>")
# for i in range(len(a)//2):
#     if a[i] != a[-(i+1)]:
#         print("不是")
#         break
# else:
#     print("是")
# for i in  range(100,1000):
#     a=i//100
#     b =i//10%10
#     c =i %10
#     d=a**3+b**3+c**3
#     if d==i:
#         print(i)
# for i in range(1,10):
#     for j in  range(1,i+1):
#         print("{}*{}={}".format(j,i,i*j),end="\t")
#     print("")
# import  random
# a= random .randrange(1,10)
# for i in  range(3):
#     b = input(">>")
#     b=int(b)
#     if a < b:
#         print("大")
#     elif a > b:
#         print("小")
#     else:
#         print("答对了")
# a=[45,78,45,69,32,45,78,69]
# for i in  a:
#     b=a.count(i)
#     if b>1:
#         for j in  range(b-1):
#             a.remove(i)
# print(a)
# a=[8,9,5]
# a.sort()
# if a[0]+a[1] > a[2]:
#     if  a[0]**2 +a[1]**2 == a[2]**2:
#         print("直角三角形")
#     elif a[0]**2 +a[1]**2 < a[2]**2:
#         print("钝角三角形")
#     else:
#         print("锐角三角形")
# else:
#     print("不是三角形")
# a=[12,45,67,94,12,35,80,94]
# a.sort()
# b=len(a)
# for i,j in enumerate(a):
#     if b - i < 3:
#         print(i,j,b)#
# from  ee import *
# import  random
# import copy
# try:
#     a = 122 + "sdxd"
#     print(a)
# except Exception as e:
#   print(e)
# else:
#     print("322")
# finally:
#     print("ooo")
# import xlwt
# f = xlwt.Workbook(encoding="utf_8")
# sheet=f.add_sheet("python_test")
# for i in range(1,10):
#     for j in range(1,i+1):
#      sheet.write(i-1,j-1,"{}*{}={}".format(i, j, i * j))
# #     sheet.write("\n")
# # sheet.write(i,0,i+1)
# f.save("qq.xls")
# import xlrd
# f= xlrd.open_workbook("aaa.xlsx")
# b= f.nsheets
# sheet = f.sheets()[1]
# rint(b)
# b= f.sheets_names()
# print(b)
#b=f.sheet_names()
# sheet =f.sheet_by_name("Sheet5")
# b = sheet.nrows
# for i in range (14,21):
#  b = sheet.row_values(i)
# print(b)

# import xlwt
# f = xlwt.Workbook(encoding="utf_8")
# sheet=f.add_sheet("python_test")
# for i in range(5):
#  for j in range(4):
#   sheet.write(i,j,"{},{},{},{}")
# f.save("qq.xls")
# import xlrd
# f= xlrd.open_workbook("aaa.xlsx")
# sheet =f.sheet_by_name("Sheet5")
# b = sheet.nrows
# b = sheet.row_values(i)
# print(b)

# import paramiko
# ssh123 = paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname="192.168.0.102",port=22,username="root",password="123456")
# a,b,c=ssh123.exec_command("ls -al /home")
# print(b.read().decode())

# import paramiko
# qq = paramiko.Transport("192.168.0.200")
# qq.connect(username="root",password="123456789")
# sftp=paramiko.SFTPClient.from_transport(qq)
# sftp.get("/home/a.sh","b.sh")
# qq.close()

# import smtplib
# import email.mime.multipart as  mul
# import  email.mime.text as text
# message = mul.MIMEMultipart()
# message["subject"] = "python_test"
# ww="dingyuchang@163.com"
# ee="15226018652@163.com","1363747969@qq.com"
# message["From"]=ww
# message["To"]=".".join(ee)
# txt = """ 良辰美景"""
# tet = text.MIMEText(txt)
# message.attach(tet)
# att1 = text.MIMEText(open('ee.py', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="day1.py"'
# message.attach(att1)
# smtp123=smtplib.SMTP_SSL("smtp.163.com",465)
# smtp123.login(ww,"dyc1997")
# smtp123.sendmail(ww,ee,message.as_string())
# smtp123.close()

# import  socket
# s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(("192.168.0.62",3000))
# s.listen(3)
# while True:
#     client,addr = s.accept()
#     reg = client.recv(1024)
#     print(reg.decode("utf-8"))
#     msg =input(">>>")
#     client.send(msg.encode("utf-8"))

# a="123"
# c=0
# for i,j in enumerate(a):
#     for f in  range(10):
#         if str(f) == j :
#             c += f*10**(len(a)-1-i)
# print(c)


# import  xlrd
# f= xlrd.open_workbook()

# def a(x,y):
#     for i in range(len(x)):
#         for j in range(len(x)):
#             if x[i] != x[j]:
#                 c=x[i]+x[j]
#                 if c==y:
#                     if x[i]<x[j]:
#                         print(x[i],x[j])
# a([12,13,14,15],27)

# import  socket
# s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(("192.168.0.82",3000))
# while True:
#     client,addr=s.recvfrom(1024)
#     print(client.decode("utf-8"))
#     msg=input(">>>")
#     s.sendto(msg.encode("utf-8"),addr)

# import  socket
# sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(("192.168.0.62",3000))
# qq="hello,kfksjfk,fbgshagfyhgas"
# sock.send(qq.encode("utf-8"))
# ww= sock.recv(1024)
# print(ww.decode("utf-8"))



# import re
# a=["fdasfs1223g","d1223as","s1356h1356"]
# # b=re.compile("1223(.*?)1356",re.S)
# # c=b.findall(a)
# # c= re.findall("1223(.*?)1356",a)
# for i in a:
#     c= re.sub("[0-9]+","asdf",i)
# print(c)

# print(hex(123))
# # print(oct(456))
# # print(bin(123))
# # print(int(0b1110111))
# # print(int(0o1110111))

# a=[chr(i) for i in range(97,103)]
# print(a)
#
# print(ord("\\"))
#
# a,b = divmod(100,16)
# print(a,b)
#
# a=int(input(">>>"))
# ff=[str(i) for i in range(10)]+[chr(g) for g in range(97,103)]
# q=""
# while True:
#     b= a % 16
#     q= q+ff[b]
#     a= a // 16
#     if a==0:
#      break
# print(q[::-1])
#
# a=int(input(">>>"))
# print(hex(a))

# class qwe():
#   def asd(self):
#    print("ni")
#    # self.rfv()
#   def qsd (self):
#    print("123")
#
#   def rfv(self):
#    print("544554")
# #
# # e=qwe()
# # e.asd()
#继承
# class qwe():
#     pass
# class iop():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def rfv(self,x,y):
#         self.age -= 10
#         print("{},血量还剩下{}".format(self.name,self.age))
#     def qaz(self):
#         self.age += 20
#         print("{},血量还剩下{}".format(self.name,self.age))
# q=iop("小明",100)
# q.rfv("10","80")
# q.qaz()


# class dte():
#     def qwe(self):
#      print("454681")
#     def zxc(self):
#         print("245485")
#
# e=dte()
# e.zxc()
#

# import  requests
# import re
# class FreeBuf():
#    def sed_qq(selt):
#      url="https://www.freebuf.com/page/1 "
#      res=requests.get(url)
#      hh=res.content.decode("utf-8")
#      return hh
#    def guolv(self, x):
#        title=[]
#        patt=re.compile('<div class="news-info">(.*?)<dd>',re.S)
#        itesms=patt.findall(x)
#        for i in itesms:
#         aa=re.findall("title=(.*?)",i)
#         title.append(aa[0])
#         return title
#    def save(self,y):
#     with open("b.txt","a",encoding="utf-8")as f:
#         for i in y:
#          f.write(i+"\n")
#
# fr = FreeBuf()
# hh=fr.sed_qq()
# yy=fr.guolv(hh)
# fr.save(yy)
# from typing import Any, Union
#
# import  requests
# import re
# url="https://www.qiushibaike.com/imgrank/page/2/"
# head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
# res = requests.get(url,headers=head)
# html=res.content.decode("utf-8")
# patt=re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg"')
# items=patt.findall(html)
# a=0
# for i in items:
#     j ="https://pic.qiushibaike.com/system/pictures/"+ i +".jpg"
#     #保存图片，先对图片连接请求，以字节的方式读取
#     msg =requests.get(j,headers=head)
#     hh = msg.content
#     with open("{}.jpg".format(a),"wb")as f :
#         f.write(hh)
#         a +=1

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
# import requests
# import re
#
# url = "https://movie.douban.com/top250?ADUIN=1004745584&ADSESSION=1556523569&ADTAG=CLIENT.QQ.5611_.0&ADPUBNO=26885"
# res = requests.get(url)
# html = res.content.decode("utf-8")
# a = re.compile(
#     '<img width="100" alt="(.*)" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/(.*).jpg" class="">')
# b = a.findall(html)
# print(b)
#
# for i in b:
#     # print(i)
#     j="https://img3.doubanio.com/view/photo/s_ratio_poster/public/{}.jpg".format(i[1])
#     print(j)
#     msg=requests.get(j)
#     hh=msg.content
#     f=open("{}.jpg".format(i[0]),"wb")
#     f.write(hh)
#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111



# url = 'https://www.qiushibaike.com/imgrank//page/2'
# head = {
# #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko) Chrome/73.0.3683.103 Safari/537.36'
# #         }
# # res = requests.get(url,headers = head)
# # html = res.content.decode('utf-8')
# patt = re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg"')#(过滤)
# itesms = patt.findall(html)
# print(len(itesms))
# for i in itesms:
#     j = 'https://pic.qiushibaike.com/system/pictures/'+i+'.jpg'
#     print(j)
# # single 2019/4/29 19:51:48
# url = 'https://movie.douban.com/top250?qq-pf-to=pcqq.group'
# head = {
#          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko) Chrome/73.0.3683.103 Safari/537.36'
#         }
# res = requests.get(url,headers = head)
# html = res.content.decode('utf-8')
# print(html)
# a=[]
# patt = re.compile('<img width="100" alt="(.*?)" ')#src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/(.*?).jpg" class="">') #(过滤)
# itesms = patt.findall(html)
# a.extend(itesms)
# p = re.compile('src="https://img(.).doubanio.com/view/photo/s_ratio_poster/public/(.*?).jpg" class=""')
# h = p.findall(html)
# b=0
# for i in h:
#     j = 'https://img{}.doubanio.com/view/photo/s_ratio_poster/public/{}.jpg'.format(i[0],i[1])
#     msg = requests.get(j,headers=head)
#     hh = msg.content
#     with open('{}.jpg'.format(a[b]),'wb') as f:
#         f.write(hh)
#     b= b+1


a=[1,2,3,4]
b=["a","c","d","f"]
e=list(zip(b,a))
print(e)