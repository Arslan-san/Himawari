# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 09:56:10 2018

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

column_name = ['terminated_count','total_count']
csv = ['only_t(age_t)','total_t(age_t)']
terminated_and_total = ['\"Termination  Reason" is not NULL and "Type" = ' + """ 'Surrender ' and """ ,'\"Termination  Reason" is not NULL and']
age = ['18-22','23-30','31-40','41-50','51-60','61-64','64']
gender = ['1','2']
for k in range(len(terminated_and_total)):
    print csv[k]
    final_frame = pd.DataFrame()
    for i in range(len(age)):
        try:
            min_age = int(age[i].split('-')[0])
            max_age = int(age[i].split('-')[1])
            pass
        except:
            pass
        for j in range(len(gender)):
            if i != len(age)-1:
                print age[i],'==>',gender[j]
                query = """
    
                       select "Policy Type Name",sum(count) as "only_termination_sum",""" + """'""" + str(gender[j]) + """'"""  +""" as "gender",""" + """'""" +  str(age[i]) + """'"""  + """ as "age"  from
                (
                	select "LatestPolicyType_01","Policy Type Name",count(*) from
                	(
                		select * from "pi_ph_seg_seg2_seg3_holder"
                		where """ + terminated_and_total[k] + """  age_t >= """ + str(min_age) + """
                		and age_t <= """ + str(max_age) + """
                		and "Policyholder'S_Gender" = """ + """'""" + str(gender[j]) + """'""" +  """
                	)as q group by q."LatestPolicyType_01",q."Policy Type Name"
    
                ) as q GROUP BY "Policy Type Name"
    
    
                 """
            else:
                print 'greater than 64','==>',gender[j]
                query = """
    
                       select "Policy Type Name",sum(count) as "only_termination_sum",""" + """'""" + str(gender[j]) + """'"""  +""" as "gender",""" + """'""" +  "greater than 64" + """'""" + """ as "age"  from
                (
                	select "LatestPolicyType_01","Policy Type Name",count(*) from
                	(
                		select * from "pi_ph_seg_seg2_seg3_holder"
                		where """ + terminated_and_total[k] + """
                         age_t > """ + str(64) + """
                		and "Policyholder'S_Gender" = """ + """'""" + str(gender[j]) + """'""" +  """
                	)as q group by q."LatestPolicyType_01",q."Policy Type Name"
    
                ) as q GROUP BY "Policy Type Name"
    
    
                 """
    
    
    
            cursor.execute(query)
            query_data = cursor.fetchall()
    
            col_names = []
            for elt in cursor.description:
                col_names.append(elt[0])
    
            query_data = pd.DataFrame(query_data,columns=col_names)
            frames = [final_frame,query_data]
            final_frame = pd.concat(frames)
            pass
        pass
    final_frame.to_csv(csv[k]+'.csv',index=False)
            
