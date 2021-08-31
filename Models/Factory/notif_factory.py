"""
    'NotifierFactory' class declares the factory method that is supposed to return an
    object of a Notifier class. 
    NotifierFactory's subclasses (Defined in '/ConcreteFactory/*') should provide the
    implementation of '_factory_method' method for its own context (variant).
"""

# Importing dependencies.
from __future__ import annotations
from abc import ABC, abstractmethod

from Exceptions import invalid_email_req
from Exceptions import invalid_post_req

from ..Interface.notif_interface import Notifier


# Importing all necessary custom exceptions for handling invalid data.
from Exceptions import invalid_email_req, invalid_post_req, invalid_sms_req


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
            result = product.notify()
            return result

        except invalid_email_req.InvalidEmailReq as e:
            # Name or Email missing, or email not correctly formatted. (REGEX fullmatch)
            return e

        except invalid_sms_req.InvalidSmsReq as e:
            # Name or sms missing or null.
            return e

        except invalid_post_req.InvalidPostReq as e:
            # Name or url missing or null. 
            return e
