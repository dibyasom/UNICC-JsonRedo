"""
    Concrete Factory override the factory method in order to change the resulting
    product's type.
"""

# Importing dependecnies and parent factory model.
from Models.Factory.notif_factory import NotifierFactory
from Models.Interface.notif_interface import Notifier
from Models.Product.email_notif import EmailNotifier

from Models.User import User


class EmailNotifierFactory(NotifierFactory):

    def __init__(self, user: User) -> None:
        self.user = user

    def _factory_method(self) -> Notifier:
        return EmailNotifier(user=self.user)
