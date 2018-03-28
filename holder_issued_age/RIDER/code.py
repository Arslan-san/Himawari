# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:56:44 2018

@author: arslan
"""

import pandas as pd
import ast
riders = pd.read_csv('MBA3_surrender_colons', sep = ':')
riders.to_csv('top_riders.csv',index=False)
policy_type = pd.read_csv('Policy Type Code.csv')


#%%
for i in range(riders.shape[0]):
    row = riders.loc[i]
    #print row
    rider_list = row.loc['top_5_rider_with_frequency']
    rider_list = ast.literal_eval(rider_list)
    list = []
    for a in rider_list:
        codes = policy_type[policy_type['Policy Type'] == a[0][:3]]
        #print codes['Policy Type'].values[0], a[0], codes['Policy Type Name'].values[0]
        list.append(tuple((codes['Policy Type Name'].values[0],a[1])))
                
    riders['top_5_rider_with_frequency'].loc[i] = list

#%%

