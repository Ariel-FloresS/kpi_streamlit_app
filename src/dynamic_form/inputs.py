from abc import ABC, abstractmethod
from typing import Union,Optional,Pattern,Any
import streamlit as st
import re

class AbstractInputCell(ABC):
    """
        Abstract base class for input cells. This class defines the interface for input cells that 
        can be used to capture user input in various formats (e.g., integer, decimal, string).

        Attributes:
            status_cell (bool): Indicates whether the input cell has been filled.
            label (str): The label for the input cell, displayed to the user.

        Methods:
            input(placeholder: Any) -> Union[Any]:
                Abstract method to capture user input, must be implemented by subclasses.
    """
    def __init__(self,label:str, status_cell:bool=False):
        self.status_cell = status_cell
        self.label = label

    @abstractmethod
    def input(self, placeholder:Any)->Union[Any]:
        """
        Abstract method to capture user input.

        Args:
            placeholder (Any): A placeholder value to display in the input field.

        Raises:
            NotImplementedError: This method must be implemented by a subclass.
        """
        raise NotImplementedError('This Method must be implemented by a subclass.')
    

class InputCellInt(AbstractInputCell):
    """
    Concrete implementation of AbstractInputCell for capturing integer input.

    Attributes:
        min_value (Optional[int]): The minimum value allowed for the input.
        max_value (Optional[int]): The maximum value allowed for the input.

    Methods:
        input(placeholder: Any) -> int:
            Captures integer input from the user.
    """

    def __init__(self, label:str, min_value:Optional[int]=None, max_value:Optional[int]=None)->None:
        super().__init__(label=label, status_cell=False)
        self.min_value = min_value
        self.max_value = max_value

    def input(self,placeholder:Any)->int:
        """
        Captures integer input from the user.

        Args:
            placeholder (Any): A placeholder value to display in the input field.

        Returns:
            int: The integer value entered by the user.
        """
        
        value = st.number_input(
            label = 'Enter a new: '+self.label,
            placeholder = 'Example: '+str(placeholder),
            value=None,
            min_value = self.min_value,
            max_value = self.max_value,
            step = 1
        )

        if value:
            # # Mark the cell as filled.
            self.status_cell = True
            return value

class InputCellDecimal(AbstractInputCell):
    """
    Concrete implementation of AbstractInputCell for capturing decimal (float) input.

    Attributes:
        min_value (Optional[float]): The minimum value allowed for the input.
        max_value (Optional[float]): The maximum value allowed for the input.

    Methods:
        input(placeholder: Any) -> float:
            Captures decimal input from the user.
    """

    def __init__(self, label:str, min_value:Optional[int]=None, max_value:Optional[int]=None)->None:
        super().__init__(label = label, status_cell=False)
        self.min_value = min_value
        self.max_value = max_value

    def input(self, placeholder:Any)->float:
        """
        Captures decimal input from the user.

        Args:
            placeholder (Any): A placeholder value to display in the input field.

        Returns:
            float: The decimal value entered by the user.
        """
        
        value = st.number_input(
            label = 'Enter a new: '+self.label,
            placeholder = 'Example: '+str(placeholder),
            value=None,
            min_value = self.min_value,
            max_value = self.max_value,
        )

        if value:
            # Mark the cell as filled.
            self.status_cell = True
            return value

class InputCellString(AbstractInputCell):
    """
        Concrete implementation of AbstractInputCell for capturing string input.

        Attributes:
            validate (Optional[Pattern[str]]): A regular expression pattern for validating the input.

        Methods:
            input(placeholder: Any) -> str:
                Captures string input from the user.
    """

    def __init__(self, label:str, validate:Pattern[str]=None)->None:
        super().__init__(label = label,  status_cell=False)
        self.validate = validate

    def input(self,placeholder:Any)->str:
        
        """
        Captures string input from the user.

        Args:
            placeholder (Any): A placeholder value to display in the input field.

        Returns:
            str: The string value entered by the user.
        """

        value = st.text_input(
            label = 'Enter a new: '+self.label,
            placeholder = 'Example: '+str(placeholder),
        )

        if value:
            # If a validation pattern is provided
            if self.validate:

                if not re.match(self.validate,value):# Validate the input.

                    st.error(f" The input value '{value}' is  not valid.")   
                else:
                    # Mark the cell as filled.
                    self.status_cell = True
                    return value
            else:
                # Mark the cell as filled.
                self.status_cell = True
                return value





