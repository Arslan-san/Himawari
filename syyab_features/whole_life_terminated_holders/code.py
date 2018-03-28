# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:54:48 2018

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

	select i."Policy Type Name", j."a_group",i."Policyholder'S_Gender",count(*)
	from "pi_ph_seg_seg2_seg3_holder" as i inner join "age_group" as j 
	on i.age between j."lower_age" and j."upper_age"
	or (i.age > j."lower_age" and j."lower_age" = 65)
	where i."Policy Type Name" = 'Whole life' and 'Terminatin  Reason' is not NULL
	--where i."Termination  Reason" is not NULL and "Type" = 'Surrender '
	group by i."Policy Type Name", j."a_group",i."Policyholder'S_Gender"
	order by i."Policy Type Name", j."a_group",i."Policyholder'S_Gender"
 
 """

cursor.execute(query)
query_data = cursor.fetchall()

col_names = []
for elt in cursor.description:
    col_names.append(elt[0])
    

query_data = pd.DataFrame(query_data,columns=col_names)
#%%

male = query_data[ query_data["Policyholder'S_Gender"] == '1']
female = query_data[ query_data["Policyholder'S_Gender"] == '2']

male['percentage'] = (male['count']/male['count'].sum()) * 100
female['percentage'] = (female['count']/female['count'].sum()) * 100

whole_life = [male,female]
whole_life = pd.concat(whole_life)

#%%
whole_life.to_csv('whole_life_terminated_stats.csv',index=False)
