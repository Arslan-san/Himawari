# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:46:40 2018

@author: arslan
"""

import psycopg2
import pandas as pd
import numpy as np
#from shapely.geometry import Point, LineString

#%%
try:
    connect_str = "dbname='himawari' user='arslan' host='localhost' password='root'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
except Exception as e:
    print(e)
    
    
query = """ 

select i."Policy Type Name", j."a_group",i."Policyholder'S_Gender","CheckupKBfirst"::int,check_up_detail,
     count(*)as "CheckupKBfirst Count"
from "pi_ph_seg_seg2_seg3_holder_new" as i inner join "age_group" as j 
on i.age between j."lower_age" and j."upper_age"
or (i.age > j."lower_age" and j."lower_age" = 65)
where i."Termination  Reason" is not NULL and "Type" = 'Surrender '
group by i."Policy Type Name", j."a_group",i."Policyholder'S_Gender","CheckupKBfirst"::int,check_up_detail
order by i."Policy Type Name", j."a_group",i."Policyholder'S_Gender","CheckupKBfirst"::int,check_up_detail

 """



cursor.execute(query)
query_data = cursor.fetchall()

col_names = []
for elt in cursor.description:
    col_names.append(elt[0])

#%%    
query_data = pd.DataFrame(query_data,columns=col_names)
#%%
query_data.to_csv('checkUP.csv',index=False)
