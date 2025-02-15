import streamlit as st
import pandas as pd
import json
from src.utils.functions import selectbox_with_a_placeholder,read_csv_file, filter_dataframe_by_a_value, chain_string_to_dict
from src.login.core import PrincipalLogin
from src.access.access_pipeline import AccessPipeline
from src.dynamic_form.form import PrincipalForm

def main():
   
    kpi_data = read_csv_file('data/KPI_Data.csv',delimiter='|')
    kp_info = read_csv_file('data/KPI_Info.csv',delimiter='|')
    role_securty = read_csv_file('data/Role_Security.csv',delimiter='|')
    user_security = read_csv_file('data/User_Security_Test.csv',delimiter='|')

    principal_login = PrincipalLogin(user_securty_dataframe = user_security)

    validator, user_email =principal_login.login()

    if validator:

        role_id = principal_login.get_RoleID(user_email = user_email)

        selection = st.pills(
            label='Select an Action',
            options=['Update KPIs', 'Enter new value to KPIs'],
            selection_mode='single'
        )
        
        match selection:

            case 'Update KPIs':
              
              access_pipeline = AccessPipeline(role_id = role_id,
                                                role_security_dataframe = role_securty,
                                                kpi_data_dataframe = kpi_data)
              manipulate_data = access_pipeline.execute()

             
              kpi_selected = selectbox_with_a_placeholder(dataframe = manipulate_data, 
                                                       column_name = 'KPI',
                                                       label='Select a KPI',
                                                       placeholder = 'Place select a KPI ...')

              if kpi_selected:
                  
                  filtered_manipulate_data = filter_dataframe_by_a_value(dataframe = manipulate_data,
                                                                         column_name = 'KPI',
                                                                         value = kpi_selected)
                  date_selected = selectbox_with_a_placeholder(dataframe = filtered_manipulate_data,
                                                            column_name = 'KPI_Value_Date',
                                                            label = 'Select a Date',
                                                            placeholder = 'Place select a Date ...')
                  if date_selected:
                      filtered_manipulate_data_by_date = filter_dataframe_by_a_value(dataframe = filtered_manipulate_data,
                                                                                     column_name = 'KPI_Value_Date',
                                                                                     value = date_selected)
                      original_dict = chain_string_to_dict((filtered_manipulate_data_by_date['KPI_Values'].values[0]))
                      input_template_dict = access_pipeline.get_input_template(kpi_info_dataframe =kp_info, kpi = kpi_selected )
                        
                      principal_form = PrincipalForm(metadata_dict=input_template_dict,original_dict=original_dict)
                      output_dict = principal_form.show()

                      if output_dict:
                          with st.spinner('Updating KPI data... Please wait.'):
                              kpi_data.loc[(kpi_data['KPI'] == kpi_selected) & (kpi_data['KPI_Value_Date'] == date_selected), 'KPI_Values'] = json.dumps(output_dict)
                              kpi_data.to_csv('data/KPI_Data.csv', sep='|')
                              st.success('KPI data updated successfully!')
             
            case 'Enter new value to KPIs':
                
                st.write('TO DO')


        

if __name__ == '__main__':
    main() 
