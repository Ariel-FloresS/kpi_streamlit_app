import pandas as pd
from typing import Tuple
from .email_validator import EmailValidator
from src.utils.functions import get_list_unique_values_from_dataframe, filter_dataframe_by_a_value

class PrincipalLogin:
    """
    A class to handle user login functionality and role retrieval based on a user security DataFrame.

    Args:
        user_securty_dataframe : pd.DataFrame
            A DataFrame containing user security information, including usernames and role IDs.

    Methods:
        login() -> Tuple[bool, str]:
            Validates the user's email against the list of emails in the DataFrame and returns a tuple indicating
            the validation result and the user's email.
        
        get_RoleID(user_email: str) -> int:
            Retrieves the Role ID associated with the given user email from the DataFrame.
    """

    def __init__(self, user_securty_dataframe:pd.DataFrame) -> None:
        """
        Constructs all the necessary attributes for the PrincipalLogin object.

        Args:
       
            user_securty_dataframe : pd.DataFrame
                A DataFrame containing user security data.
        """
        self.user_securty_dataframe = user_securty_dataframe

    def login(self) -> Tuple[bool, str]:
        """
        Validates the user's email and returns the validation result along with the email.

        This method retrieves a hardcoded email (for testing purposes) and compares it with the list of unique
        usernames from the user security DataFrame. The email validation is performed using the EmailValidator class.

        Returns:
       
            Tuple[bool, str]
                A tuple where the first element indicates if the email is valid (True/False) and the second element
                is the user's email.
        """
        # descomment this when migrating to snowflake
        # user_email = st.experimental_user.email
        # user_email = user_email.lower()

        # Hardcoded email to test this module, comment this when migrating this module to Snowflake
        user_email = 'u1@gmail.com'

        # Get the list of emails
        emails = get_list_unique_values_from_dataframe(dataframe=self.user_securty_dataframe, 
                                                       column_name='UserName')

        # Validate the email
        email_validator = EmailValidator(email=user_email, 
                                         list_of_emails=emails)

        validator = email_validator.validate()

        return validator, user_email

    def get_RoleID(self, user_email: str) -> int:
        """
        Retrieves the Role ID for a given user email.

        This method filters the user security DataFrame to find the Role ID associated with the provided email.

        Args:
        
            user_email : str
                The email of the user whose Role ID is to be retrieved.

        Returns:
        
            int
                The Role ID of the user as an integer.
        """
        filtered_user_securty_dataframe = filter_dataframe_by_a_value(dataframe = self.user_securty_dataframe,
                                                                      column_name = 'UserName',
                                                                      value = user_email)
        role_id = filtered_user_securty_dataframe['RoleID'].values
        return int(role_id[0])