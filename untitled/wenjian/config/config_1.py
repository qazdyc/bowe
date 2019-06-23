def read_data():
    datas =[ ]
    with open("/Users/dingxiaobai/PycharmProjects/untitled/wenjian/data/ssa.txt") as f:
        d=f.readlines()
    for i in d:
     return i.replace("\n","").split(",")
     return datas
    print(read_data())