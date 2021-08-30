from __future__ import annotations

"""
    The Notifier interface declares the abstract operation 'notify' and 'validate_data' that all concrete notifiers
    must implement.

    All concrete instances will implement notify() for their use case, for instance ...
    - SmsNotifier must send a sms when notify() is called upon it.
    - PostNotifier must send a POST req to API endpoint with user's data payload when notify() is called upon it.

    All concrete instances will implement validate_date() to validate the required param fot instance ...
    - SmsNotifier must not have name and phone fields as null.
"""

# Importing dependencies.
from abc import ABC, abstractmethod, abstractproperty


class Notifier(ABC):

    @abstractmethod
    def notify(self) -> str:
        pass

    @abstractmethod
    def validate_data(self) -> bool:
        pass
