# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 23:08:19 2018

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

select j."a_group",i."Policyholder'S_Gender",count(*) 
from "pi_ph_seg_seg2_seg3_holder_new" as i inner join "age_group" as j 
on i.age between j."lower_age" and j."upper_age"
or (i.age > j."lower_age" and j."lower_age" = 65)
where i."Policyholder'S_Gender" not in ('0','3')
group by j."a_group",i."Policyholder'S_Gender"
order by j."a_group",i."Policyholder'S_Gender"

 """



cursor.execute(query)
query_data = cursor.fetchall()

col_names = []
for elt in cursor.description:
    col_names.append(elt[0])

#%%    
query_data = pd.DataFrame(query_data,columns=col_names)
#%%
query_data.to_csv('overall_Demographics.csv',index=False)
