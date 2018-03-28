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

final_sheet = pd.DataFrame(index = ages, columns = products)
writer = pd.ExcelWriter('fmale_features.xlsx', engine='xlsxwriter')

for i in products:
    
    for j in ages:
 #       for k in gender:
#            total_P = data_P[(data_P['Policy Type Name'] == 'Whole life') & (data_P['a_group'] == j) & (data_P["Policyholder'S_Gender"] == k)][['LatestP_01 SUM']]
#            total_P_avg = data_P[(data_P['Policy Type Name'] == 'Whole life') & (data_P['a_group'] == j) & (data_P["Policyholder'S_Gender"] == k)][['LatestP_01 average']]
#
#            total_S = data_S[(data_S['Policy Type Name'] == 'Whole life') & (data_S['a_group'] == j) & (data_S["Policyholder'S_Gender"] == k)][['LatestS_01 SUM']]
#            total_S_avg = data_S[(data_S['Policy Type Name'] == 'Whole life') & (data_S['a_group'] == j) & (data_S["Policyholder'S_Gender"] == k)][['LatestS_01 average']]
#
#            average_duration = data_insurance_duration[(data_insurance_duration['Policy Type Name'] == 'Whole life') & (data_insurance_duration['a_group'] == j) & (data_insurance_duration["Policyholder'S_Gender"] == k)][['average']]
#
#            channel = data_channel[(data_channel['Policy Type Name'] == 'Whole life') & (data_channel['a_group'] == j) & (data_channel["Policyholder'S_Gender"] == k)]#[['application Channel Count']]
#            channel = channel.dropna(axis=0, how='any')               
#            channel = channel.nlargest(3, 'application Channel Count')
#
#            reason = data_t_reason[(data_t_reason['Policy Type Name'] == 'Whole life') & (data_t_reason['a_group'] == j) & (data_t_reason["Policyholder'S_Gender"] == k)]#[['application Channel Count']]
#            reason = reason.dropna(axis=0, how='any')               
#            reason = reason.nlargest(3, 'Termination Reason  Count')
#
#            address_count = address[(address['Policy Type Name'] == 'Whole life') & (address['a_group'] == j) & (address["Policyholder'S_Gender"] == k)]#[['application Channel Count']]
#            address_count = address_count.dropna(axis=0, how='any')               
#            address_count = address_count.nlargest(3, 'address Count')
    
    
            

        
            total_P = data_P[(data_P['Policy Type Name'] == i) & (data_P['a_group'] == j) & (data_P["Policyholder'S_Gender"] == 2)][['LatestP_01 SUM']]
            
            total_P_avg = data_P[(data_P['Policy Type Name'] == i) & (data_P['a_group'] == j) & (data_P["Policyholder'S_Gender"] == 2)][['LatestP_01 average']]
            
            
            if total_P.shape[0] == 0:
                total_P = 0
                total_P_avg = 0
                
            else:
                
                total_P = "{:,}".format(int(round(total_P.values[0][0])))
                total_P_avg = "{:,}".format(int(round( total_P_avg.values[0][0])))
                
            total_S = data_S[(data_S['Policy Type Name'] == i) & (data_S['a_group'] == j) & (data_S["Policyholder'S_Gender"] == 2)][['LatestS_01 SUM']]
                        
            total_S_avg = data_S[(data_S['Policy Type Name'] == i) & (data_S['a_group'] == j) & (data_S["Policyholder'S_Gender"] == 2)][['LatestS_01 average']]
            
            
            if total_S.shape[0] == 0:
                total_S = 0
                total_S_avg = 0
                pass
            else:
                
                total_S = "{:,}".format(int(round(total_S.values[0][0]))   )
                
                total_S_avg = "{:,}".format(int(round(total_S_avg.values[0][0])) ) 
                
            average_duration = data_insurance_duration[(data_insurance_duration['Policy Type Name'] == i) & (data_insurance_duration['a_group'] == j) & (data_insurance_duration["Policyholder'S_Gender"] == 2)][['average']]
            
            
            
            if average_duration.shape[0] == 0:
                average_duration = 0
                pass
            else:
                
                average_duration = "{:,}".format(int(round(average_duration.values[0][0])) )
                


            channel = data_channel[(data_channel['Policy Type Name'] == i) & (data_channel['a_group'] == j) & (data_channel["Policyholder'S_Gender"] ==2)]#[['application Channel Count']]
            channel = channel.dropna(axis=0, how='any')               
            channel = channel.nlargest(3, 'application Channel Count')

            reason = data_t_reason[(data_t_reason['Policy Type Name'] == i) & (data_t_reason['a_group'] == j) & (data_t_reason["Policyholder'S_Gender"] == 2)]#[['application Channel Count']]
            reason = reason.dropna(axis=0, how='any')               
            reason = reason.nlargest(3, 'Termination Reason  Count')

            address_count = address[(address['Policy Type Name'] == i) & (address['a_group'] == j) & (address["Policyholder'S_Gender"] == 2)]#[['application Channel Count']]
            address_count = address_count.dropna(axis=0, how='any')               
            address_count = address_count.nlargest(3, 'address Count')
            
            a,b,c = '','',''
            
            
            for row in range(channel.shape[0]):
#                a = a + str(row+1) + '-' + str(channel.iloc[row]['Details']) + """ (highest) -- corresponding code """ + str(channel.iloc[row]['application Channel']) + '\n'
                a = a + str(row+1) + '- ' +  str(channel.iloc[row]['detail']) + """ -- corresponding code """ + str(channel.iloc[row]['application Channel']) + '\n    '
                pass            
            for row in range(reason.shape[0]):
                b = b + str(row+1) + '- ' + str(reason.iloc[row]['Details']) + """ -- corresponding code """ + str(reason.iloc[row]['Termination  Reason']) + '\n    '
                pass            
            for row in range(address_count.shape[0]):
                c = c + str(row+1) + '- ' + str(address_count.iloc[row]['address_name']) + '\n    ' 
                pass

            if channel.shape[0] == 0:
                a = 'No application channel used'
                pass
            if reason.shape[0] == 0:
                b = 'No termination reason'
                pass
            if address_count.shape[0] == 0:
                c = 'No address'
                pass
            
            

        
            print total_P, total_P_avg, total_S, total_S_avg, average_duration
            
#            if reason.shape[0] >= 3 and channel.shape[0] >= 3 and address_count.shape[0] >= 3:
                
            
#                feature = """
#                            •Premium Paid:
#                                1- Total P(1) premium is """ + str(total_P.values[0][0]) + """ Yen
#                                2- Total P(1) premium average """ + str(total_P_avg.values[0][0]) + """ Yen
#                            •Settlement Amount:
#                                1-  Total Settlement is """ + str(total_S.values[0][0]) + """ Yen
#                                 2- Settlement Average """ + str(total_S_avg.values[0][0]) + """ Yen
#                            • Average Policy Validations period """ + str(average_duration.values[0][0]) + """ years
#                            • Most application Channel Used: 
#                               1-  Existing Policyholder (higest) -- corresponding code """ + str(channel.iloc[0]['application Channel']) + """
#                                2- Oneself / living relatives(2nd highest) -- corresponding code """ + str(channel.iloc[1]['application Channel']) + """
#                                3- Friends/acquaintance/Family/Relative (3rd highest) -- corresponding code """ + str(channel.iloc[2]['application Channel']) + """
#                            • Most Common Termination Causes: 
#                                1- """ + str(reason.iloc[0]['Details']) + """ (highest) -- corresponding code """ + str(reason.iloc[0]['Termination  Reason']) + """ 
#                                2- """ + str(reason.iloc[1]['Details']) + """ (2nd highest) -- corresponding code """ + str(reason.iloc[1]['Termination  Reason']) + """
#                                3- """ + str(reason.iloc[2]['Details']) + """ (3rd highest) -- corresponding code """ + str(reason.iloc[2]['Termination  Reason']) + """
#    
#                            • Most Common Cities: 
#                                1- """ + str(address_count.iloc[0]['address_name']) + """ (highest) 
#                                2- """ + str(address_count.iloc[1]['address_name']) + """ (2nd highest) 
#                                3- """ + str(address_count.iloc[2]['address_name']) + """ (3rd highest) 
#      
#                          
#                            """
            
            feature = """•Premium Paid:
    1- Total P(1) premium is """ + str(total_P) + """ Yen
    2- Total P(1) premium average """ + str(total_P_avg) + """ Yen \n
•Settlement Amount:
    1- Total Settlement is """ + str(total_S) + """ Yen
    2- Settlement Average """ + str(total_S_avg) + """ Yen \n
• Average Policy Validations period """ + str(average_duration) + """ years 

• Most application Channel Used: 
    """ + a + """ 
• Most Common Termination Causes:  
    """ + b + """
• Most Common Cities:
    """ + c + """  """
                      
                        
                        
            final_sheet[i].loc[j] = feature
#            break
#        break
#    break

#%%

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

final_sheet.to_excel(writer, sheet_name='Sheet1')
writer.save()

#final_sheet.to_excel('junk.xlsx',encoding='utf-8')

            

        
