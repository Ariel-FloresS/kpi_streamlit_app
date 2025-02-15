from .generate_inputs import InputGenerator
from src.utils.functions import transform_dictionary_to_pandas
import streamlit as st
import copy

class PrincipalForm:
    """
    The PrincipalForm class is responsible for creating and managing a dynamic form based on metadata. 
    It allows users to input values and compare original and updated data.

    Attributes:
        metadata_dict (dict): A dictionary containing metadata about the input fields.
        original_dict (dict): A dictionary containing the original values for the input fields.

    Methods:
        __init__(metadata_dict: dict, original_dict: dict) -> None:
            Initializes the PrincipalForm with metadata and original dictionaries.

        dynamic_form() -> dict:
            Generates a dynamic form and captures user input.

        comparative_tables(dict_updated: dict) -> None:
            Displays comparative tables of original and updated data.

        show() -> dict:
            Displays the form and handles user interactions.
    """

    def __init__(self, metadata_dict:dict, original_dict:dict)->None:
        self.metadata_dict = metadata_dict
        self.original_dict = original_dict

    def dynamic_form(self)->dict:
        """
        Generates a dynamic form and captures user input.

        Returns:
            dict: A dictionary containing updated values from the input fields.
        """
        # Create a deep copy of the original dictionary.
        st.session_state.dict_updated = copy.deepcopy(self.original_dict)

        # Create an InputGenerator instance.
        input_generator = InputGenerator(metadata_dict = self.metadata_dict)
        
        # Generate input cells based on metadata.
        list_of_inputs = input_generator.generate()

        for input_cell in list_of_inputs:

            if not input_cell.status_cell: # If the cell has not been filled.

                new_value = input_cell.input(placeholder = self.original_dict.get(input_cell.label)) # Capture input.

                if new_value:
                    st.write(f'the new value is: {new_value}')# Display the new value.
                else:
                    st.warning('Please fill the cell')# Warn if the cell is empty.

            if input_cell.status_cell:
                st.session_state.dict_updated[input_cell.label] = new_value # Update the dictionary with new values

        return st.session_state.dict_updated
    
    def comparative_tables(self,dict_updated)->None:
        """
        Displays comparative tables of original and updated data.

        Args:
            dict_updated (dict): A dictionary containing updated values for the input fields.
        """

        original_dataframe = transform_dictionary_to_pandas(dictionary = self.original_dict)
        updated_dataframe = transform_dictionary_to_pandas(dictionary = dict_updated)

        # Create two columns for comparison.
        col1, col2 = st.columns(spec = 2, border=True)

        with col1:
            st.header('Prevous data.')
            st.dataframe(data = original_dataframe, hide_index = True)
        with col2:
            st.header('Updated data.')
            st.dataframe(data = updated_dataframe, hide_index =True)
    
    def show(self)->dict:
        """
        Displays the form and handles user interactions.

        Returns:
            dict: A dictionary containing updated values from the input fields.
        """
        with st.container(border=True):    
        
            st.markdown('<h1 style="color: black; font-weight: bold;">Form to update a KPI</h1>', unsafe_allow_html=True)

            dict_updated = self.dynamic_form()
            
            self.comparative_tables(dict_updated = dict_updated)

            summited_button = st.button(label = 'Update KPI')

            if summited_button:
                return dict_updated
            
            
            
        
            
            

            
            

        





