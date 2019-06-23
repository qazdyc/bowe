
#socket通信客户端
import  socket
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=("192.168.0.82",3000)
msg=input(">>>")
s.sendto(msg.encode("utf-8"),host)
reg=s.recv(1024)
print(reg.decode("utf-8"))

# import requests
# import re
# head = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko) Chrome/73.0.3683.103 Safari/537.36'
#        }
# def getHeml(head,num):
#     html=requests.get\
#         ("http://sou.zhaopin.com/jobs/searchresult.ashx?jl=全国&kw=python&sb=1&sm=0&isfilter=0&fl=489&isadv=0&sg=9115fea9f0cd4119949b3ddecba0e984&p=%s"%(num),headers=head)
#     html.encoding=html.apparent_encoding
#     return html.content
# str3='<li class="newlist_deatil_two"><span>地点：(.*?)</span><span>公司性质：(.*?)</span><span>公司规模：(.*?)</span><span>经验：(.*?)</span><span>学历：(.*?)</span><span>职位月薪：(.*?)</span><li class="newlist_deatil_last">'
# zz=re.compile(str3)
# d=dict()
# def action():
#     for pagenum in range(90):
#         html=getHeml(head,pagenum)
#         xinxi=re.findall(zz,html)
#         for x in xinxi:
#             #说明：0代表地址，1为企业性质，2为企业规模，3为要求经验，4为要求最低学历,5,职位月薪
#             if d.get(x[0]) is None:
#                d[x[0]]=1
#             else:
#                 d[x[0]]=d[x[0]]+1
#                 #print val
#             print x[0]+" "+x[1]+" "+x[2]+" "+x[3]+" "+x[4]+" "+x[5]
# if __name__=="__main__":
#  action()
import requests
import json
url='https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&=0&_v=0.80226492&x-zp-page-request-id=f14ab29fd9c84c6987a2d1a82d7259ab-1557219520461-956404'
head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
res = requests.get(url,headers=head)
p=res.content.decode('utf-8')
aa = json.loads(p)
f=open('b.txt','w+',encoding='utf-8')
for  i in range(0,90):
    b1=aa['data']['results'][i]['company']['name']
    b2=aa['data']['results'][i]['jobName']
    b3=aa['data']['results'][i]['salary']
    b4=aa['data']['results'][i]['city']['display']
    b5=aa['data']['results'][i]['eduLevel']['name']
    f.write("{},".format(b1))
    f.write("{},".format(b2))
    f.write("{},".format(b3))
    f.write("{},".format(b4))
    f.write("{}".format(b5))
    f.write('\n')
f=open('b.txt','r',encoding='utf-8')
a=f.readlines()
import pymysql
import xlwt
ww=xlwt.Workbook('a5.xls')
sheet=ww.add_sheet('zhilian')
c=["公司ID","岗位名称","薪资","公司地点","学历"]
for k in range(len(c)):
    sheet.write(0,k,c[k])
for l in range(0,len(a)):
    bb=a[l].split(',')
    for a1 in range(len(c)):
        sheet.write(l+1,a1,bb[a1])
ww.save('a.xls')
conn=pymysql.connect(host='192.168.0.200',port=3306,user='root',passwd='123456')
m=conn.cursor()
m.execute('use test')
m.execute('create table zhilian(公司ID  char(45),岗位名称 char(35),薪资 char(15),公司地点 char(10),学历 char(10))')
for j in range(0,len(a)):
    bb=a[j].split(',')
    m.execute('insert into zhilian values("{}","{}","{}","{}","{}");'.format(bb[0],bb[1],bb[2],bb[3],bb[4]))
