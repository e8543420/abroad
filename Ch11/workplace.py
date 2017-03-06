# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:35:19 2017

@author: zhaox
"""

import pypyodbc
from pandas import DataFrame,Series
import pandas as pd
import numpy as np

#%% 读取数据库，形成pandas格式frame
fileName='C:\\info.mdb'

conn = pypyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + fileName)
cur = conn.cursor()

cur.execute('''SELECT a_exp,t_pno,t_cou,t_des3,t_fee,p_sex,p_marry,p_fla,p_work FROM (abroad
               LEFT JOIN team ON abroad.a_team=team.t_no)
               LEFT JOIN persons ON abroad.a_user=persons.p_user''')  #access 处理leftjoin时，需要在第一个join子句加括号
#列表表头：职务，团组编号，姓名，同行人数，地点，出访目的，出发时间，回国时间，邀请单位，经费来源，经费来源机构，性别，生日，婚姻，学位，语言，语言流利度，毕业院校，所属学院
list_db=cur.fetchall()
frame_db=pd.DataFrame(list_db,columns=['a_exp','t_pno','t_cou','t_des3','t_fee','p_sex','p_marry','p_fla','p_work'])

frame_db.to_csv('aaa.csv',encode='utf-8')

