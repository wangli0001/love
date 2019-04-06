import os 
import csv
import pandas as pd 
import numpy as np
from os import listdir
path = "E:\\1234"
for info in os.listdir(path):    
    print(info)
    domain = os.path.abspath('E:\\1234')   #获取文件夹的路径 
    info = os.path.join(domain,info)
    file =open(info,'r')
    #print(info)
    lines=file.readlines()
    row=[]#定义行数组
    column=[]#定义列数组
    data_1=[]
    data_2=[]
    data=[]
    output=[]
  
    with open('info', 'w', newline="") as f:
        for line in lines:
            row.append(line.split(','))#以“，”为分隔符分隔
        for col in row:
            data=[col[0],col[8]]
            if data[1]!='':
                data_1.append(data[0])
                data_2.append(data[1]) 
        for i in range(len(data_2)):
            data_3=[data_1[i],data_2[i]]

            outname = open('info.csv','a', newline='')
            csv_write = csv.writer(outname,dialect='excel')
            csv_write.writerow(data_3)
    
#             column.extend(data_3)
#             csv.writer(f).writerow((data_3))
          
                
#     dataframe = pd.DataFrame({'hour':col[0],'glu':col[8]},index=[0])
# #         outname = info.replace('info','outname')
# #将DataFrame存储为csv,index表示是否显示行名，default=Tru
#     dataframe.to_csv('info.csv',index=False,sep=',')