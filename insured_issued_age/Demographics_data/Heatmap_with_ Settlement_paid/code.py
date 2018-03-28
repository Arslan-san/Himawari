# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 01:56:08 2018

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

select i."perfecture_name",sum(split_part("LatestS_01",'.',1)::int)
from "pi_ph_seg_seg2_seg3_insured_new" as i 
group by i."perfecture_name"
order by i."perfecture_name"

 """



cursor.execute(query)
query_data = cursor.fetchall()

col_names = []
for elt in cursor.description:
    col_names.append(elt[0])

#%%    
query_data = pd.DataFrame(query_data,columns=col_names)
#%%
query_data.to_csv('Heatmap_with_Settlement_paid.csv',index=False)
