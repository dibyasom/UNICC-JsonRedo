"""
    'NotifierFactory' class declares the factory method that is supposed to return an
    object of a Notifier class. 
    NotifierFactory's subclasses (Defined in '/ConcreteFactory/*') should provide the
    implementation of '_factory_method' method for its own context (variant).
"""

# Importing dependencies.
from __future__ import annotations
from abc import ABC, abstractmethod

from ..Interface.notif_interface import Notifier


# Importing all necessary custom exceptions for handling invalid data.
from Exceptions.invalid_email_req import InvalidEmailReq
from Exceptions.invalid_post_req import InvalidPostReq
from Exceptions.invalid_sms_req import InvalidSmsReq


class NotifierFactory(ABC):

    @abstractmethod
    def _factory_method(self) -> Notifier:
        pass

    # Instantiate the required variant and send notifications if param is valid for the context.
    def notify_job(self) -> str:

        product: Notifier = self._factory_method()
        try:
            # validata_data raises custom exceptions defined in '/Exceptions/', and notify() is never called for such entries.
            product.validate_data()

            # Abstract method defined in interface, and implemented by concrete instances.
            # Hence, can be used in unified way to notify() regardless of sms, phone, or url.
            print(product.notify())

        except InvalidEmailReq as e:
            # Name or Email missing, or email not correctly formatted. (REGEX fullmatch)
            print(e)

        except InvalidSmsReq as e:
            # Name or sms missing or null.
            print(e)

        except InvalidPostReq as e:
            # Name or url missing or null.
            print(e)
