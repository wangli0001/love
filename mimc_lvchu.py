# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:35:08 2019

@author: hp
"""
import pandas as pd
import csv
file =open('mimc_ts.csv','r')
lines=file.readlines()#读取所有行
file.close()
row=[]#定义行数组
column=[]#定义列数组
with open('exp.csv', 'w', newline="") as f:
    for line in lines:
        row.append(line.split(','))#以“，”为分隔符分隔

    for col in row:
        data=[col[0],col[8]]
        column.extend(data)
        csv.writer(f).writerow((data))
       
        dataframe = pd.DataFrame({'hour':col[0],'glu':col[8]},index=[0])#取数据

        dataframe.to_csv("exp.csv",index=True,sep=',')
