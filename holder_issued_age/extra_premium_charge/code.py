# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:57:03 2018

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


select q."Policy Type Name", q."a_group",q."Policyholder'S_Gender" ,sum(q.count) as "count" from
(

	select i."Policy Type Name", j."a_group",i."Policyholder'S_Gender",substring(split_part("Extra Premium ChargeCD",'.',1) from 1 for 1)::int as "Extra Premium ChargeCD" ,count(*)
	from "pi_ph_seg_seg2_seg3_holder_new" as i inner join "age_group" as j 
	on i.age between j."lower_age" and j."upper_age"
	or (i.age > j."lower_age" and j."lower_age" = 65)
	where i."Termination  Reason" is not NULL and "Type" = 'Surrender ' and substring(split_part("Extra Premium ChargeCD",'.',1) from 1 for 1)::int is not null
	group by i."Policy Type Name", j."a_group",i."Policyholder'S_Gender", substring(split_part("Extra Premium ChargeCD",'.',1) from 1 for 1)::int
	order by i."Policy Type Name", j."a_group",i."Policyholder'S_Gender", substring(split_part("Extra Premium ChargeCD",'.',1) from 1 for 1)::int

) as q group by q."Policy Type Name", q."a_group",q."Policyholder'S_Gender"


 """



cursor.execute(query)
query_data = cursor.fetchall()

col_names = []
for elt in cursor.description:
    col_names.append(elt[0])

#%%    
query_data = pd.DataFrame(query_data,columns=col_names)
query_data.to_csv('extra_premium_charge_count.csv',index=False)