"""
    Notifier provide various implementations of the Product interface.
"""

# For simulated delay.
from time import sleep

# User object for storing data.
from Models.User import User

# Importing one unified interface 'Notifier' for using any factory method.
from ..Interface.notif_interface import Notifier

# Fetch constants
from constants import SIMULATED_NETWORK_DELAY

# Importing custom exception for this context (EmailNotifier)
from Exceptions.invalid_email_req import InvalidEmailReq


def validate():
    pass


class EmailNotifier(Notifier):

    def __init__(self, user: User) -> None:
        self.user = user

    # Implement abstract method validate_data to validate data critical to this context.
    def validate_data(self) -> bool:
        if self.user.name == None or self.user.email == None:
            raise InvalidEmailReq(self.user.getData())

    # Implement abstract method for the required context.
    def notify(self) -> str:
        # Simulated delay to mimic a network call.
        sleep(SIMULATED_NETWORK_DELAY)
        return f"EMAIL sent to {self.user.email}. Data: {self.user.getData()}"
