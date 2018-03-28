# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:27:18 2018

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

select i."Policy Type Name",
     count(split_part(i."LatestS_01",'.',1)::int)as "LatestS_01 Count",
     sum(split_part(i."LatestS_01",'.',1)::int) as "LatestS_01 SUM",
     avg(split_part(i."LatestS_01",'.',1)::int) as "LatestS_01 average"  
from "pi_ph_seg_seg2_seg3_holder_new" as i

group by i."Policy Type Name" -- , j."a_group",i."Policyholder'S_Gender"
order by i."Policy Type Name" -- , j."a_group",i."Policyholder'S_Gender"
 
 
 """



cursor.execute(query)
query_data = cursor.fetchall()

col_names = []
for elt in cursor.description:
    col_names.append(elt[0])

#%%    
query_data = pd.DataFrame(query_data,columns=col_names)
#%%
query_data.to_csv('Lates_S.csv',index=False)
