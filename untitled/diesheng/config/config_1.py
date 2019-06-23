def read_data():
    datas =[ ]
    with open("/Users/dingxiaobai/PycharmProjects/untitled/diesheng/data/dxb.txt") as f:
        d=f.readlines()
    for i in d:
     return i.replace("\n","").split(",")
     return datas
     print(read_data())

