"""
    Notifier provide various implementations of the Product interface.
"""

# For simulated delay.
from time import sleep

# User object for storing data.
from Models.User import User

# Importing one unified interface 'Notifier' for using any factory method.
from Models.Interface.notif_interface import Notifier

# Fetch constants
from constants import *

# Importing custom exception for this context (EmailNotifier)
from Exceptions.invalid_email_req import InvalidEmailReq

# Importing Regular Expressions to validate email
import re


def validate():
    pass


class EmailNotifier(Notifier):

    # Regex for validating email string
    # (STATIC Attribute, since allocating one to every instance would be waste of memory)
    EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Returns true for correctly formatter email.
    def email_validator(email_str): return re.fullmatch(
        EmailNotifier.EMAIL_REGEX, email_str)

    def __init__(self, user: User) -> None:
        self.user = user

    # Implementing abstract method validate_data to validate data critical to this context.
    def validate_data(self) -> bool:

        # Checking email and name are non null, and validating email string.
        if not (self.user.name != None and self.user.email != None and EmailNotifier.email_validator(self.user.email)):
            raise InvalidEmailReq(self.user.getData())

    # Implement abstract method for the required context.
    def notify(self) -> str:
        # Simulated delay to mimic a network call.
        sleep(SIMULATED_NETWORK_DELAY)
        return f"{ANSI_SUCCESS_NOTIF}EMAIL sent to {self.user.email}. Data: {self.user.getData()}{ANSI_END}"
