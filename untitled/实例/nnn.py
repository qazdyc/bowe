#不用int变成整数
# a="123"
# b=a[::-1]
# s=0
# for i,j in enumerate(b):
#     for h in  range(10):
#         if str(h)==j:
#             s+=h*10**i
# print(s)
#
# #九九乘法表
# for i in  range(1,10):
#     for j in  range(1,i+1):
#         print("{}*{}={}".format(i,j,i*j),end="\t")
#     print("")

#创建目录在目录中创建a.txt文件，先文件中写入多行数据
# import os
# os.mkdir('aaa')
# with open('a8.txt','w',encoding='utf-8')as f:
#     for i in range(10):
#         f.write("asdsa"+"\n")

#将a.txt文件中的数据添加到数据库中
# import pymysql
# with open('a8.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# noon=pymysql.connect(host='192.168.0.200',port=3306,user='root',passwd='123456')
# m=noon.cursor()
# m.execute('use test')
# for i in range(len(a)):
#
#     c=a[i].split(',')
#     if i==0:
#         m.execute('create table wqe({} char(255),{} char(255),{} char(255),{} char(255));'.format(c[0],c[1],c[2],c[3]))
#     else:
#         m.execute('insert into wqe values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
# m.execute('select * from wqe ')
# d=m.fetchall()
# print(d)
# noon.close()






# import smtplib
# import email.mime.multipart as  mul
# import  email.mime.text as text
# message = mul.MIMEMultipart()
# message["subject"] = "python_test"
# ww="dingyuchang@163.com"
# ee="1363747969@qq.com","825069672@qq.com"
# message["From"]=ww
# message["To"]=".".join(ee)
# txt = """ 良辰美景"""
# tet = text.MIMEText(txt)
# message.attach(tet)
# att1 = text.MIMEText(open('ee.py', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="day1.py"'
# message.attach(att1)
# smtp123=smtplib.SMTP_SSL("smtp.163.com",465)
# smtp123.login(ww,"dyc1997")
# smtp123.sendmail(ww,ee,message.as_string())
# smtp123.close()
#
#socket通信服务器
import  socket
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.0.82",3000))
while True:
    client,addr=s.recvfrom(1024)
    print(client.decode("utf-8"))
    msg=input(">>>")
    s.sendto(msg.encode("utf-8"),addr)



import  requests
import re
class FreeBuf():
   def sed_qq(selt):
     url="https://sou.zhaopin.com/ "
     res=requests.get(url)
     hh=res.content.decode("utf-8")
     return hh
   def guolv(self, x):
       title=[]
       patt=re.compile('<div class="news-info">(.*?)<dd>',re.S)
       itesms=patt.findall(x)
       for i in itesms:
        aa=re.findall("title=(.*?)",i)
        title.append(aa[0])
        return title
   def save(self,y):
    with open("b.txt","a",encoding="utf-8")as f:
        for i in y:
         f.write(i+"\n")

fr = FreeBuf()
hh=fr.sed_qq()
yy=fr.guolv(hh)
fr.save(yy)