# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 08:15:21 2019

@author: hp
"""

import os
import re
file_path = os.listdir('E:\\test')  #路径
for filename in file_path:
    #print(filename)
    portion = os.path.splitext(filename)
    #print(portion)
    if portion[1] == '.txt':
         match = re.match('.*(\d).*',portion[0])
         #print(match)
         pb = match.group(1)
         if str(pb) in portion[0]:
            new = 'visit_' + str(pb)          
            newname = new + portion[1]
            os.rename(filename, newname)
  