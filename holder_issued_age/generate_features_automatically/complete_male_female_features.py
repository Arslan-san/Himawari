# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:36:26 2018

@author: arslan
"""

import pandas as pd

data_P = pd.read_csv('Lates_P.csv')
data_S = pd.read_csv('Lates_S.csv')
data_channel = pd.read_csv('application_channel_count.csv')
data_t_reason = pd.read_csv('termination_reason_count.csv') 
data_insurance_duration = pd.read_csv('average_duration.csv')
address = pd.read_csv('age_wise_address_count.csv')
apl_count = pd.read_csv('apl_count.csv')
extrta_charge = pd.read_csv('extra_premium_charge_count.csv')
top_riders = pd.read_csv('top_riders.csv',sep=':')
top_riders['average_number_riders'] = top_riders['average_number_riders'].fillna(0)




excel_sheet = pd.read_excel('E_report_image_03.xlsx', sheetname='Surrender Rate')

#%%

products = ['Whole life',
 'Term life',
 'M.I.P',
 'Cancer',
 'Nursing care',
 'Medical',
 'Female Disease',
 'Dread Disease W.L.',
 'Dread Disease T.L.',
 'Maternity Insurance(or New Pregnant Woman Insurance)',
 'Inc. Dec. Term Life',
 'Joint life(Flexible)',
 'J.M.I.P',
 'Endowment',
 'Juvenile',
 'Annuity(Annuity Certain )',
 'Annuity(Whole Life Annuity With Guaranteed Installment )',
 'Injury',
 'Medical（Coins） ',
 'Joint life',
 'VL Whole life',
 'VL Endowment']
ages = list(data_channel['a_group'].unique())
gender = list(data_channel["Policyholder'S_Gender"].unique())
gender = [1,2]
csv = ['male_features.xlsx','female_features.xlsx']
csv_index = 0
for g in gender:
    final_sheet = pd.DataFrame(index = ages, columns = products)
    writer = pd.ExcelWriter(csv[csv_index], engine='xlsxwriter')
    for i in products:    
        for j in ages:
            
                total_P = data_P[(data_P['Policy Type Name'] == i) & (data_P['a_group'] == j) & (data_P["Policyholder'S_Gender"] == g)][['LatestP_01 SUM']]
                
                total_P_avg = data_P[(data_P['Policy Type Name'] == i) & (data_P['a_group'] == j) & (data_P["Policyholder'S_Gender"] == g)][['LatestP_01 average']]
                
                
                if total_P.shape[0] == 0:
                    total_P = 0
                    total_P_avg = 0
                    
                else:
                    total_P = "{:,}".format(int(round(total_P.values[0][0]))) 
                    total_P_avg = "{:,}".format(int(round(total_P_avg.values[0][0])))
                    
                total_S = data_S[(data_S['Policy Type Name'] == i) & (data_S['a_group'] == j) & (data_S["Policyholder'S_Gender"] == g)][['LatestS_01 SUM']]
                            
                total_S_avg = data_S[(data_S['Policy Type Name'] == i) & (data_S['a_group'] == j) & (data_S["Policyholder'S_Gender"] == g)][['LatestS_01 average']]
                
                
                if total_S.shape[0] == 0:
                    total_S = 0
                    total_S_avg = 0
                    pass
                else:
                    total_S = "{:,}".format(int(round(total_S.values[0][0])))     
                    total_S_avg = "{:,}".format(int(round(total_S_avg.values[0][0])) )
                    
                average_duration = data_insurance_duration[(data_insurance_duration['Policy Type Name'] == i) & (data_insurance_duration['a_group'] == j) & (data_insurance_duration["Policyholder'S_Gender"] == g)][['average']]
                
                if average_duration.shape[0] == 0:
                    average_duration = 0
                    pass
                else:
                    average_duration = "{:,}".format(int(round(average_duration.values[0][0])) )
                    
                charge = extrta_charge[(extrta_charge['Policy Type Name'] == i) & (extrta_charge['a_group'] == j) & (extrta_charge["Policyholder'S_Gender"] == g)][['count']]
    
                if charge.shape[0] == 0:
                    charge = 0
                    pass
                else:
                    charge = "{:,}".format(int(round(charge.values[0][0])) )
    
                
    
    
                channel = data_channel[(data_channel['Policy Type Name'] == i) & (data_channel['a_group'] == j) & (data_channel["Policyholder'S_Gender"] ==g)]#[['application Channel Count']]
                channel = channel.dropna(axis=0, how='any')               
                channel = channel.nlargest(3, 'application Channel Count')
    
                reason = data_t_reason[(data_t_reason['Policy Type Name'] == i) & (data_t_reason['a_group'] == j) & (data_t_reason["Policyholder'S_Gender"] == g)]#[['application Channel Count']]
                reason = reason.dropna(axis=0, how='any')               
                reason = reason.nlargest(3, 'Termination Reason  Count')
    
                address_count = address[(address['Policy Type Name'] == i) & (address['a_group'] == j) & (address["Policyholder'S_Gender"] == g)]#[['application Channel Count']]
                address_count = address_count.dropna(axis=0, how='any')               
                address_count = address_count.nlargest(3, 'address Count')
                
                top_3_count = apl_count[(apl_count['Policy Type Name'] == i) & (apl_count['a_group'] == j) & (apl_count["Policyholder'S_Gender"] == g)]
                top_3_count = top_3_count.nlargest(3,'count')
    
                t_riders = top_riders[(top_riders['policy_type'] == i) & (top_riders['age_group'] == j) & (top_riders["gender"] == g)][['average_number_riders','top_5_rider_with_frequency']]
                rider_withOut_Nan = t_riders.dropna(axis=0, how='any')
                if rider_withOut_Nan.shape[0] != 0:
                    rider = rider_withOut_Nan['top_5_rider_with_frequency'].values[0].split('-')
                    pass
                else:
                    rider = []
                    
                rider_avg = t_riders['average_number_riders']
               
                if rider_avg.shape[0] == 0:
                    rider_avg = 0
                else:
                    rider_avg = rider_avg.values[0]
    
    
                a,b,c,d,e = '','','','',''
                
                
                for row in range(channel.shape[0]):
                    a = a + str(row+1) + '- ' + str(channel.iloc[row]['detail']) + """ -- corresponding  code """ + str(channel.iloc[row]['application Channel']) + '\n    '
                    pass            
                for row in range(reason.shape[0]):
                    b = b + str(row+1) + '- ' + str(reason.iloc[row]['Details']) + """ -- corresponding code """ + str(reason.iloc[row]['Termination  Reason']) + '\n    '
                    pass            
                for row in range(address_count.shape[0]):
                    c = c + str(row+1) + '- ' + str(address_count.iloc[row]['perfecture_name']) + '\n    ' 
                    pass
    
                for row in range(top_3_count.shape[0]):
                    d = d + str(row+1) + '- ' + str(top_3_count.iloc[row]['APL Number of LOAN']) + '   (count ' +str(top_3_count.iloc[row]['count']) + ')' + '\n    ' 
                    pass
                
                for row in range(len(rider)):
                    e = e + str(row+1) + '- ' + str(rider[row])  + '\n    '
                    pass
     
    
                if channel.shape[0] == 0:
                    a = '- No Application Channel used\n'
                    pass
                if reason.shape[0] == 0:
                    b = '- No Termination Reason\n'
                    pass
                if address_count.shape[0] == 0:
                    c = '- No Perfecture Against This Policy \n'
                    pass
    
                if top_3_count.shape[0] == 0:
                    d = '- No APL LOAN \n'
                    pass
                
                if len(rider) == 0:
                    e = '- No Riders Against This Policy \n'
                    pass
                
    
            
                
                feature = """•Premium paid:
    1- Total premium is """ + str(total_P) + """ Yen
    2- Average premium paid is """ + str(total_P_avg) + """ Yen \n
•Settlement amount:
    1- Total settlement is """ + str(total_S) + """ Yen
    2- Average settlement paid is """ + str(total_S_avg) + """ Yen \n
• Average Policy retention period """ + str(average_duration) + """ Months 

• The most utilized application channel: 
    """ + a + """ 
• The most common termination causes:  
    """ + b + """
• The most common prefectures:
    """ + c + """  
• The most common numbers of APL loan:
    """ + d + """    

• Number of customers charged with extra premium, based on high risk, is """ + str(charge) + """:
       
• Top riders against this policy (Policy Type, Count):      
    """ + e + """    
• Average number of riders purchased with this policy is """ + str(rider_avg) + """
        

    """

                          
                            
                            
                final_sheet[i].loc[j] = feature
        
    import sys  
    
    reload(sys)  
    sys.setdefaultencoding('utf8')
    
    final_sheet.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    csv_index = csv_index + 1

#final_sheet.to_excel('junk.xlsx',encoding='utf-8')

