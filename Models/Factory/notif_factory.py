"""
    The Creator class declares the factory method that is supposed to return an
    object of a Notifier class. 
    The Creator's subclasses (Defined in '/ConcreteFactory/*') should provide the
    implementation of '_factory_method' method for its specific use case.
"""

# Importing dependencies.
from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty

from ..Interface.notif_interface import Notifier

from ..User import User

# Importing all necessary custom exceptions for handling data invalidation.
from Exceptions.invalid_email_req import InvalidEmailReq
from Exceptions.invalid_post_req import InvalidPostReq
from Exceptions.invalid_sms_req import InvalidSmsReq


class Creator(ABC):

    @abstractmethod
    def _factory_method(self) -> Notifier:
        pass

    # Instantiate the required variant and send notifications if param is valid for the context.
    def notify_job(self) -> str:

        product: Notifier = self._factory_method()
        try:
            product.validate_data()

            # validata_data raises custom exceptions defined in '/Exceptions/', and notify() is never called for such entries.
            return product.notify()

        except InvalidEmailReq as e:
            print(e)
        except InvalidSmsReq as e:
            print(e)
        except InvalidPostReq as e:
            print(e)
