"""
    Concrete Factory override the factory method in order to change the resulting
    product's type.
"""

# Importing dependecnies and parent factory model.
from ..Factory.notif_factory import Creator
from ..Interface.notif_interface import Notifier
from ..Product.post_notif import PostNotifier

from Models.User import User


class PostNotifierFactory(Creator):

    def __init__(self, user: User) -> None:
        self.user = user

    def _factory_method(self) -> Notifier:
        return PostNotifier(user=self.user)
