from .inputs import AbstractInputCell, InputCellInt, InputCellDecimal, InputCellString
from typing import List

class InputGenerator:
    """
    The InputGenerator class is responsible for generating input cells based on a metadata dictionary. 
    It creates a list of input cells for different data types.

    Attributes:
        metadata_dict (dict): A dictionary containing metadata about the input fields.
        input_list (List[AbstractInputCell]): A list to store generated input cell instances.

    Methods:
        __init__(metadata_dict: dict) -> None:
            Initializes the InputGenerator with a metadata dictionary.

        generate() -> List[AbstractInputCell]:
            Generates a list of input cells based on the metadata dictionary.
    """

    def __init__(self,metadata_dict:dict)->None:
        self.metadata_dict = metadata_dict
        self.input_list = []

    def generate(self)->List[AbstractInputCell]:
        """
            Generates a list of input cells based on the metadata dictionary.

            Returns:
                List[AbstractInputCell]: A list of instances of input cell classes.
            
            Raises:
                ValueError: If the data type in the metadata dictionary is not recognized.
        """

        for key, value in self.metadata_dict.items():
           
            match value:

                case 'int':
                    self.input_list.append(
                        InputCellInt(label = key)# Create an integer input cell.
                    )
                case 'decimal' | 'float':

                    self.input_list.append(
                        InputCellDecimal(label = key) # Create a decimal input cell.
                    )
                case 'str':
                    self.input_list.append(
                        InputCellString(label = key) # Create a string input cell.
                    )
                case _:
                    raise ValueError(f"The data type '{value}' is not recognized. Please implement the class for this input type.")
                
        return self.input_list
