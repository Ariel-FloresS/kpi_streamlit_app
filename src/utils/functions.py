import pandas as pd
import streamlit as st
import ast
from typing import List, Any

def read_csv_file(path: str, delimiter: str = '|') -> pd.DataFrame:
    """
    Reads a CSV file with a specified delimiter.

    Args:
        path (str): The file path of the CSV file to be read.
        delimiter (str): The delimiter used in the CSV file (default is '|').

    Returns:
        pd.DataFrame: A DataFrame containing the data from the CSV file.
    """
    try:
        return pd.read_csv(filepath_or_buffer=path, delimiter=delimiter)
    except Exception as e:
        raise Exception(f"An error occurred while reading the CSV file: {e}")
        

def get_list_unique_values_from_dataframe(dataframe: pd.DataFrame, column_name: str) -> List[Any]:
    """
    Returns a list of unique values from a specified column in the DataFrame.

    Args:
        dataframe (pd.DataFrame): The DataFrame from which to retrieve unique values.
        column_name (str): The name of the column from which to extract unique values.

    Returns:
        List[Any]: A list of unique values from the specified column.
    """
    try:
        if column_name not in dataframe.columns:
            raise TypeError(f"The column '{column_name}' does not exist in the DataFrame.")
        return dataframe[column_name].unique().tolist()
    except Exception as e:
        raise Exception(f"An error occurred while retrieving unique values: {e}")
        

def filter_dataframe_by_a_value(dataframe: pd.DataFrame, column_name: str, value: Any) -> pd.DataFrame:
    """
    Filters the DataFrame by a specific value in a specified column.

    Args:
        dataframe (pd.DataFrame): The DataFrame to filter.
        column_name (str): The name of the column to filter by.
        value (Any): The value to filter the DataFrame on.

    Returns:
        pd.DataFrame: A DataFrame containing only the rows where the specified column matches the given value.
    """
    try:
        mask = dataframe[column_name] == value
        return dataframe[mask]
    except Exception as e:
        raise Exception(f"An error occurred while filtering the DataFrame: {e}")
       
def chain_string_to_list(chain: str) -> list:
    """
    Converts a string representation of a list into an actual Python list.

    Args:
        chain (str): A string representation of a list (e.g., "[1, 2, 3]").

    Returns:
        list: A Python list converted from the string, or an empty list if conversion fails.
    """
    try:
        # Use ast.literal_eval to safely evaluate the string as a Python literal
        lst = ast.literal_eval(chain)
        return lst
    except (ValueError, SyntaxError) as e:
        raise Exception(f"The string is not in the correct format to convert to a list: {e}")
       

def chain_string_to_dict(chain: str) -> dict:
    """
    Converts a string representation of a dictionary into an actual Python dictionary.

    Args:
        chain (str): A string representation of a dictionary (e.g., "{'key': 'value'}").

    Returns:
        dict: A Python dictionary converted from the string, or an empty dictionary if conversion fails.
    """
    try:
        # Use ast.literal_eval to safely evaluate the string as a Python literal
        dictionary = ast.literal_eval(chain)
        return dictionary
    except (ValueError, SyntaxError) as e:
        raise Exception(f"The string is not in the correct format to convert to a dictionary: {e}")
       

def selectbox_with_a_placeholder(dataframe: pd.DataFrame, column_name: str, label: str, placeholder: str) -> Any:
    """
    Creates a select box with a placeholder based on unique values from a specified column in the DataFrame.

    Args:
        dataframe (pd.DataFrame): The DataFrame from which to retrieve unique values.
        column_name (str): The name of the column to get unique values for the select box.
        label (str): The label displayed for the select box.
        placeholder (str): The placeholder text displayed in the select box.

    Returns:
        Any: The selected option from the select box.
    """
    try:
        options_list = get_list_unique_values_from_dataframe(dataframe=dataframe, column_name=column_name)
        option = st.selectbox(label=label, options=options_list, placeholder=placeholder, index=None)
        return option
    except Exception as e:
        raise Exception(f"An error occurred while creating the select box: {e}")
        

def transform_dictionary_to_pandas(dictionary: dict) -> pd.DataFrame:
    """
    Transforms a dictionary into a pandas DataFrame.

    Args:
        dictionary (dict): The dictionary to convert into a DataFrame.

    Returns:
        pd.DataFrame: A DataFrame created from the dictionary.
    """
    try:
        return pd.DataFrame(dictionary, index=[0])
    except Exception as e:
        raise Exception(f"An error occurred while transforming the dictionary to a DataFrame: {e}")
    

       