# coding:utf-8
import pypyodbc
from pandas import DataFrame,Series
import pandas as pd
import numpy as np

def count_split(input_frame,spliter):
    temp=[]
    for x in input_frame.dropna():
        temp=temp+x.split(spliter)
    temp=Series(temp)
    output=temp.value_counts()
    return output


#%% 读取数据库，形成pandas格式frame
fileName='C:\\info.mdb'

conn = pypyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + fileName)
cur = conn.cursor()

cur.execute('''SELECT a_exp,a_team,t_nam,t_pno,t_cou,t_des3,t_dat,t_datend,t_inv,t_fee,t_fee2,p_sex,p_date,p_marry,p_ade,p_lag,p_fla,p_eback,p_work FROM (abroad
               LEFT JOIN team ON abroad.a_team=team.t_no)
               LEFT JOIN persons ON abroad.a_user=persons.p_user''')  #access 处理leftjoin时，需要在第一个join子句加括号
#列表表头：职务，团组编号，姓名，同行人数，地点，出访目的，出发时间，回国时间，邀请单位，经费来源，经费来源机构，性别，生日，婚姻，学位，语言，语言流利度，毕业院校，所属学院
list_db=cur.fetchall()

frame_db=pd.DataFrame(list_db,columns=['a_exp','a_team','t_nam','t_pno','t_cou','t_des3','t_dat','t_datend','t_inv','t_fee','t_fee2','p_sex','p_date','p_marry','p_ade','p_lag','p_fla','p_eback','p_work'])

#%% 统计数量(总)
#clean_t_cou=frame_db['t_cou'].fillna('Missing')
#clean_t_cou[clean_t_cou == '']='空'
#count_cou=frame_db['t_cou'].value_counts()
#t_cou_counts[:10].plot(kind='barh',rot=0)  #绘图
count_cou=count_split(frame_db.t_cou,'，')
count_exp=frame_db['a_exp'].value_counts()
count_des3=frame_db['t_des3'].value_counts()
count_fee=count_split(frame_db.t_fee,', ')
count_ade=frame_db['p_ade'].value_counts()
count_lag=frame_db['p_lag'].value_counts()
count_work=frame_db['p_work'].value_counts()

#%% 统计数量(分年)
t_year=Series([x.year for x in frame_db.t_dat])
frame_db['t_year']=t_year
grouped_db=frame_db.groupby('t_year')
count_y_cou=grouped_db['t_cou'].apply(count_split,'，').unstack().fillna(0).T
count_y_exp=grouped_db['a_exp'].apply(count_split,'，').unstack().fillna(0).T
count_y_des3=grouped_db['t_des3'].apply(count_split,'，').unstack().fillna(0).T
count_y_fee=grouped_db['t_fee'].apply(count_split,', ').unstack().fillna(0).T
count_y_ade=grouped_db['p_ade'].apply(count_split,'，').unstack().fillna(0).T
count_y_lag=grouped_db['p_lag'].apply(count_split,'，').unstack().fillna(0).T
count_y_work=grouped_db['p_work'].apply(count_split,'，').unstack().fillna(0).T


