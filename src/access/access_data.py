import streamlit as st
import pandas as pd
from typing import List

from src.utils.functions import chain_string_to_list, filter_dataframe_by_a_value
class AccessData:
    """
    The AccessData class is responsible for retrieving data related to user roles and KPIs. 
    It initializes with a role ID and provides methods to fetch KPIs associated with that role.

    Attributes:
        role_id (int): The Role ID of the user.

    Methods:
        __init__(role_id: int) -> None:
            Initializes AccessData with a role ID.

        get_list_kpis_from_role(role_security_dataframe: pd.DataFrame) -> List[str]:
            Retrieves a list of KPIs associated with the user's role.

        get_interactable_kips_dataframe(kpis_list_from_role: List[str], kpi_data_dataframe: pd.DataFrame) -> pd.DataFrame:
            Retrieves a DataFrame of interactable KPIs based on the role's KPIs.
    """

    def __init__(self, role_id:int)->None:
        self.role_id = role_id

    def get_list_kpis_from_role(self, role_security_dataframe:pd.DataFrame)->List[str]:
        """
        Retrieves a list of KPIs associated with the user's role.

        Args:
            role_security_dataframe (pd.DataFrame): DataFrame containing role security information.

        Returns:
            List[str]: A list of KPI names associated with the user's role.
        """
        # Filter the role security dataframe to find the row corresponding to the role ID.
        filtered_role_security_dataframe = filter_dataframe_by_a_value(dataframe = role_security_dataframe,
                                                                       column_name = 'RoleID',
                                                                       value = self.role_id
                                            )
        # Extract the role name from the filtered dataframe.
        role = filtered_role_security_dataframe['Role'].values
        st.write(f'Your currect role is: {role[0]}')

        # Extract the KPIs associated with the role and return them as a list.
        kpis_list_of_string = filtered_role_security_dataframe['KPIs'].values
        return chain_string_to_list(chain = kpis_list_of_string[0])
    
    def get_interactable_kips_dataframe(self,kpis_list_from_role:List[str],kpi_data_dataframe:pd.DataFrame)->pd.DataFrame:
        """
        Retrieves a DataFrame of interactable KPIs based on the role's KPIs.

        Args:
            kpis_list_from_role (List[str]): A list of KPI IDs associated with the user's role.
            kpi_data_dataframe (pd.DataFrame): DataFrame containing KPI data.

        Returns:
            pd.DataFrame: A DataFrame containing only the interactable KPIs based on the role's KPIs.
        """
        # Return a filtered dataframe containing only the KPIs that are interactable based on the role's KPIs.
        return kpi_data_dataframe[kpi_data_dataframe['KPI_Id'].isin(kpis_list_from_role)]



