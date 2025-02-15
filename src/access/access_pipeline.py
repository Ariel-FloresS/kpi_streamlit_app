import pandas as pd
from .access_data import AccessData
from src.utils.functions import chain_string_to_dict,filter_dataframe_by_a_value

class AccessPipeline:
    """
    The AccessPipeline class manages the process of accessing Key Performance Indicators (KPIs) 
    based on user roles. It provides methods to execute the access process and retrieve input templates 
    for specific KPIs based on the user's role.

    Attributes:
        role_id (int): The ID of the user role.
        role_security_dataframe (pd.DataFrame): DataFrame containing role security information.
        kpi_data_dataframe (pd.DataFrame): DataFrame containing KPI data.

    Methods:
        __init__(role_id: int, role_security_dataframe: pd.DataFrame, kpi_data_dataframe: pd.DataFrame) -> None:
            Initializes the AccessPipeline with role ID and dataframes.
            
        execute() -> pd.DataFrame:
            Executes the pipeline to retrieve a DataFrame of interactable KPIs based on the user's role.
            
        get_input_template(kpi_info_dataframe: pd.DataFrame, kpi: str) -> dict:
            Retrieves the input template for a specific KPI.
    """

    def __init__(self,role_id:int, role_security_dataframe:pd.DataFrame, kpi_data_dataframe:pd.DataFrame)->None:
        self.role_id = role_id
        self.role_security_dataframe = role_security_dataframe
        self.kpi_data_dataframe = kpi_data_dataframe

    def execute(self)->pd.DataFrame:
        """
        Executes the pipeline to retrieve a DataFrame of interactable KPIs based on the user's role.

        Returns:
            pd.DataFrame: A DataFrame containing the interactable KPIs.
        """
        # Create an instance of AccessData with the given role ID.
        access_data = AccessData(role_id = self.role_id)

        # Get the list of KPIs associated with the role from the role security dataframe.
        interact_kpis_list = access_data.get_list_kpis_from_role(role_security_dataframe = self.role_security_dataframe)

        # Retrieve the interactable KPI dataframe based on the KPIs list and the KPI data dataframe.
        interactable_kips_dataframe =  access_data.get_interactable_kips_dataframe(kpis_list_from_role = interact_kpis_list,
                                                                              kpi_data_dataframe = self.kpi_data_dataframe)
        return interactable_kips_dataframe
    
    def get_input_template(self,kpi_info_dataframe:pd.DataFrame, kpi:str)->dict:
        """
        Retrieves the input template for a specific KPI.

        Args:
            kpi_info_dataframe (pd.DataFrame): DataFrame containing KPI information.
            kpi (str): The name of the KPI for which to retrieve the input template.

        Returns:
            dict: A dictionary representing the input template for the specified KPI.
        """
        # Filter the KPI info dataframe to find the row corresponding to the specified KPI name.
        filtered_kpi_info_dataframe = filter_dataframe_by_a_value(dataframe = kpi_info_dataframe,
                                                                  column_name = 'KPI_Name',
                                                                  value = kpi)
        # Extract the metadata associated with the filtered KPI.
        template_input_list_of_string = filtered_kpi_info_dataframe['Meta_Data'].values
        
        # Return the input template as a dictionary.
        input_template = chain_string_to_dict(template_input_list_of_string[0])
        return input_template


        

