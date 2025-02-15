import streamlit as st
from typing import List

class EmailValidator:
    """
    A class to validate if an email is in the list of authorized emails.
    """

    def __init__(self, email: str, list_of_emails: List[str]) -> None:
        """
        Initializes the EmailValidator with the provided email and list of authorized emails.

        Args:
            email (str): The email address to validate.
            list_of_emails (List[str]): A list of authorized email addresses.
        """
        self.email = email  # Store the email to be validated
        self.list_of_emails = list_of_emails  # Store the list of authorized emails

    def validate(self) -> bool:
        """
        Validates if the email is in the list of authorized emails.

        Returns:
            bool: True if the email is authorized, False otherwise.
        """
        # Check if the provided email is not in the list of authorized emails
        if self.email not in self.list_of_emails:
            # Display an error message if access is denied
            st.error("You don't have access to this Application")
            return False  # Return False if the email is not authorized
        else:
            welcom_message = f"""
                <div style="background-color: #ADD8E6; color: black; padding: 10px; border-radius: 8px; font-size: 14px; text-align: center; font-weight: bold;">
                    Welcome <span style="color: #1E90FF;">{self.email}</span>!
                </div>
            """
            st.markdown(body = welcom_message,unsafe_allow_html=True)
            return True  # Return True if the email is authorized