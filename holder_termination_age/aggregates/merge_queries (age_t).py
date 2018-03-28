# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:13:21 2018

@author: arslan
"""


import psycopg2
import pandas as pd
import numpy as np

try:
    connect_str = "dbname='himawari' user='arslan' host='localhost' password='root'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
except Exception as e:
    print(e)

column_names = ['"APL Number of LOAN"','"TotalP_1"','"APL Cumulative Balance"','"APL Number of Payment"']
age = ['18-22','23-30','31-40','41-50','51-60','61-64','64']
#age = ['18-22']
gender = ['1','2']
final_frame = pd.DataFrame()
for i in range(len(column_names)):
    print column_names[i]
    for j in range(len(age)): 
        try:
            min_age = int(age[j].split('-')[0])
            max_age = int(age[j].split('-')[1])
            pass
        except:
            pass
        for k in range(len(gender)):
            
            if j != len(age)-1:
                print age[j],'==>',gender[k]
                query = """ 
                select "Policy Type Name",
                count(split_part(""" + column_names[i] + """,'.',1)::int)as count,
                sum(split_part(""" + column_names[i] + """,'.',1)::int) as sum,
                avg(split_part(""" + column_names[i] + """,'.',1)::int) as average,
                min(split_part(""" + column_names[i] + """,'.',1)::int) as min,
                max(split_part(""" + column_names[i] + """,'.',1)::int) as max,
                percentile_cont(0.5)WITHIN group(order by NULLIF(split_part(""" + column_names[i] + """,'.',1)::int ,0)) as median,
                mode() within group (order by NULLIF(split_part(""" + column_names[i] + """,'.',1)::int, 0)) as mode,
                """ + """'""" + str(gender[k]) + """'"""  +""" as "gender",
                """ + """'""" +  str(age[j]) + """'"""  + """ as "age",
                """ + """'""" +  column_names[i].split('"')[1] + """'"""  +  """ as attribute_value
                
                
                from "pi_ph_seg_seg2_seg3_holder"
                where "Termination  Reason" is not NULL and 
                    "Type" = 'Surrender ' and
                    age_t >= """ + str(min_age) + """ and 
                    age_t <= """ + str(max_age) + """ and 
                    "Policyholder'S_Gender" = """ + """'""" + str(gender[k]) + """'""" +  """
                group by "Policy Type Name" 
    
                 """   
            else:
                print age[j],'==>',gender[k]
                query = """ 
                select "Policy Type Name",
                count(split_part(""" + column_names[i] + """,'.',1)::int)as count,
                sum(split_part(""" + column_names[i] + """,'.',1)::int) as sum,
                avg(split_part(""" + column_names[i] + """,'.',1)::int) as average,
                    min(split_part(""" + column_names[i] + """,'.',1)::int) as min,
                max(split_part(""" + column_names[i] + """,'.',1)::int) as max,
                percentile_cont(0.5)WITHIN group(order by NULLIF(split_part(""" + column_names[i] + """,'.',1)::int ,0)) as median,
                mode() within group (order by NULLIF(split_part(""" + column_names[i] + """,'.',1)::int, 0)) as mode,
                """ + """'""" + str(gender[k]) + """'"""  +""" as "gender",
                """ + """'""" +  "greater than 64" + """'"""  + """ as "age",
                """ + """'""" +  column_names[i].split('"')[1] + """'"""  +  """ as attribute_value
                
                
                from "pi_ph_seg_seg2_seg3_holder"
                where "Termination  Reason" is not NULL and "Type" = 'Surrender ' and
                    age_t > """ + str(64) + """ and 
                    "Policyholder'S_Gender" = """ + """'""" + str(gender[k]) + """'""" +  """
                group by "Policy Type Name" 
    
                 """   
         
            cursor.execute(query)
            query_data = cursor.fetchall()
            
            col_names = []
            for elt in cursor.description:
                col_names.append(elt[0])

            
            query_data = pd.DataFrame(query_data,columns=col_names)
            frames = [final_frame,query_data]
            final_frame = pd.concat(frames)
            #final_frame = query_data
                        
final_frame.to_csv('final_data.csv',index=False)                  

