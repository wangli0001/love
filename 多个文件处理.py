import os 
import re
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
    portion = os.path.splitext(info)
    if portion[1] == '.csv':
         match = re.match('.*(\d).*',portion[0])
         #print(match)
         pb = match.group(1)
         if str(pb) in portion[0]:
            new = 'visit_' + str(pb)          
            newname = new + portion[1]
            print(newname)
            #os.rename(filename, newname)
  
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

            outname = open(newname,'a', newline='')
            csv_write = csv.writer(outname,dialect='excel')
            csv_write.writerow(data_3)
    
#           