# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:12:37 2018

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

select i."Policy Type Name", j."a_group",i."Policyholder'S_Gender",split_part("APL Number of LOAN",'.',1)::int as "APL Number of LOAN",count(*)
from "pi_ph_seg_seg2_seg3_holder_new" as i inner join "age_group" as j 
on i.age between j."lower_age" and j."upper_age"
or (i.age > j."lower_age" and j."lower_age" = 65)
where i."Termination  Reason" is not NULL and "Type" = 'Surrender '
group by i."Policy Type Name", j."a_group",i."Policyholder'S_Gender",split_part("APL Number of LOAN",'.',1)::int
order by i."Policy Type Name", j."a_group",i."Policyholder'S_Gender",split_part("APL Number of LOAN",'.',1)::int

 """



cursor.execute(query)
query_data = cursor.fetchall()

col_names = []
for elt in cursor.description:
    col_names.append(elt[0])

#%%    
query_data = pd.DataFrame(query_data,columns=col_names)
query_data.to_csv('apl_count.csv',index=False)
#products = ['Whole life',
# 'Term life',
# 'M.I.P',
# 'Cancer',
# 'Nursing care',
# 'Medical',
# 'Female Disease',
# 'Dread Disease W.L.',
# 'Dread Disease T.L.',
# 'Maternity Insurance(or New Pregnant Woman Insurance)',
# 'Inc. Dec. Term Life',
# 'Joint life(Flexible)',
# 'J.M.I.P',
# 'Endowment',
# 'Juvenile',
# 'Annuity(Annuity Certain )',
# 'Annuity(Whole Life Annuity With Guaranteed Installment )',
# 'Injury',
# 'Medical（Coins） ',
# 'Joint life',
# 'VL Whole life',
# 'VL Endowment']
#ages = list(query_data['a_group'].unique())
#gender = list (query_data["Policyholder'S_Gender"].unique())
#%%

#for i in products:
#    for j in ages:
#        for k in ['1','2']:
#            
#           data = query_data[(query_data['Policy Type Name'] == i) & (query_data['a_group'] == j) & (query_data["Policyholder'S_Gender"] == k)]
#           data = data.nlargest(3,'count')
#           
#        break
#    break





#%%
