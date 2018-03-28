# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 01:10:53 2018

@author: arslan
"""

import psycopg2
import pandas as pd
import numpy as np
#from shapely.geometry import Point, LineString

poplation = pd.read_csv('poplation.csv')

#%%
try:
    connect_str = "dbname='himawari' user='arslan' host='localhost' password='root'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
except Exception as e:
    print(e)
    
    
query = """ 

select i."perfecture_name",count(*)
from "pi_ph_seg_seg2_seg3_insured_new" as i 

where (i."Termination  Reason" in ('G31','G32','G33','G34','G35','G36','G37') 
or i."Termination  Reason" in ('G41','G42','G43','G44') 
or i."Termination  Reason" in ('G52','G53') 
or i."Termination  Reason" in ('GA1','GA2') 
or i."Reduce Settlement Reason" = 'DA1')


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
query_data['percentage'] = 0
for i in range(len(query_data['perfecture_name'])):
    denominator = poplation[poplation['Prefectures'] == query_data['perfecture_name'].loc[i]]['population']
    if (len(denominator) != 0):
	    denominator = int(denominator.values[0].replace(',','')) 
	    #print float(query_data['count'].loc[i]) , '/' ,float(denominator)  
	    query_data['percentage'].loc[i] = (float((float(query_data['count'].loc[i]))/float(denominator)))*100
#%%
query_data.to_csv('Heatmap_with_ surrender.csv',index=False)
