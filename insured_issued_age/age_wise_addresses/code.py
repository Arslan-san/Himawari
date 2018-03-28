# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 18:07:35 2018

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

select i."Policy Type Name", j."a_group",i."Insured'S Gender","perfecture_name",
     count(*) as "address Count"
from "pi_ph_seg_seg2_seg3_insured_new" as i inner join "age_group" as j 
on i.age between j."lower_age" and j."upper_age"
or (i.age > j."lower_age" and j."lower_age" = 65)



where i."Termination  Reason" in ('G31','G32','G33','G34','G35','G36','G37') 
        or i."Termination  Reason" in ('G41','G42','G43','G44') 
        or i."Termination  Reason" in ('G52','G53') 
        or i."Termination  Reason" in ('GA1','GA2') 
        or i."Reduce Settlement Reason" = 'DA1'

group by i."Policy Type Name", j."a_group",i."Insured'S Gender","perfecture_name"
order by i."Policy Type Name", j."a_group",i."Insured'S Gender","perfecture_name"


 """



cursor.execute(query)
query_data = cursor.fetchall()

col_names = []
for elt in cursor.description:
    col_names.append(elt[0])
query_data = pd.DataFrame(query_data,columns=col_names)
query_data.to_csv('age_wise_address_count.csv',index=False)
