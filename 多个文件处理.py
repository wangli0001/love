import os 
import csv
import pandas as pd 
path = "E:/1234/"
for info in os.listdir(path): 
    domain = os.path.abspath('E:/1234/')  #获取文件夹的路径 
    info = os.path.join(domain,info) #将路径与文件名结合起来就是每个文件的完整路径 
    data1 = pd.read_csv(info) 
    lines=data1.readlines()#读取所有行
    row=[]#定义行数组
    column=[]#定义列数组
    with open(info, 'w', newline="") as f:
        for line in lines:
            row.append(line.split(','))#以“，”为分隔符分隔
        for col in row:
            data2=[col[0],col[8]]
            column.extend(data2)
            csv.writer(f).writerow((data2))
       
            dataframe = pd.DataFrame({'hour':col[0],'glu':col[8]},index=[0])#取数据
            dataframe.to_csv(info,index=True,sep=',')
