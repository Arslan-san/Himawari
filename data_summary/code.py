# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 10:13:43 2018

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
    
final_frame = pd.DataFrame()
#array = [
#
#'"RevivalNumberKB"',
#'"Revival Reason"',
#'"Extra Premium ChargeCD"',
#'"Termination  Reason"',
#'"Latest Payment Completion Reason"',
#'"Recovery Reason"',
#'"Reduce Settlement Reason"',
#'"An increase Reason"',
#'"CheckupKBfirst"',
#'"application Channel"',
#'"PledgeSettingKB"',
#'"LatestAgencyD_01"',
#'"LatestAgentCD_01"',
#'"LatestAgencyD_02"',
#'"LatestAgentCD_02"',
#'"LatestAGSelf-ContractsKB_01"',
#
#]

array = [

'"LatestPolicyType_01"',
'"LatestPolicyType_02"',
'"LatestPolicyType_03"',
'"LatestPolicyType_04"',
'"LatestPolicyType_05"',
'"LatestPolicyType_06"',
'"LatestPolicyType_07"',
'"LatestPolicyType_08"',
'"LatestPolicyType_09"',
'"LatestPolicyType_10"',
'"LatestPolicyType_11"',
'"LatestPolicyType_12"',
'"LatestPolicyType_13"',
'"LatestPolicyType_14"',
'"LatestPolicyType_15"',
'"LatestPolicyType_16"',
'"LatestPolicyType_17"',
'"LatestPolicyType_18"',
'"LatestPolicyType_19"',
'"LatestPolicyType_20"',
'"Solo ProprietorshipKB"',
'"APL Number of LOAN"',
'"APL Number of Payment"',
'"APL Cumulative Balance"',
'"Policy LoanKB"',
'"Policy Loan Number of LOAN"',
'"Claim ClassificationKB"',
'"LatestPayment Method"',
'"LatestAdvance Premium Term"',
'"LifeStyleDiseaseUnInsuredCD1"',
'"LifeStyleDiseaseUnInsuredTerm1"',
'"LifeStyleDiseaseUnInsuredCD2"',
'"LifeStyleDiseaseUnInsuredTerm2"',
'"LifeStyleDiseaseUnInsuredCD3"',
'"LifeStyleDiseaseUnInsuredTerm3"',
'"LifeStyleDiseaseUnInsuredCD4"',
'"LifeStyleDiseaseUnInsuredTerm4"',
'"Disease UnInsuredCD1"',
'"Disease UnInsuredTerm1"',
'"Disease UnInsuredCD2"',
'"Disease UnInsuredTerm2"',
'"Disease UnInsuredCD3"',
'"Disease UnInsuredTerm3"',
'"Disease UnInsuredCD4"',
'"Disease UnInsuredTerm4"'

]
    

for i in array:    
    query = """ 
    
    select """ + i + """ as "distinct_values",count(*) , """ + i.replace('"',"""'""") + """ as "column_name"  from "pi_ph_seg_seg2_seg3_holder"
    group by """ + i + """ order by "distinct_values"
    
     """
    
    cursor.execute(query)
    query_data = cursor.fetchall()
    
    col_names = []
    for elt in cursor.description:
        col_names.append(elt[0])
        
    
    query_data = pd.DataFrame(query_data,columns=col_names)
    frames = [final_frame,query_data]
    final_frame = pd.concat(frames)
#%%
final_frame.to_csv('merged_data_summary.csv',index=False)