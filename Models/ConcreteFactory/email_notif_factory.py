# Importing dependecnies and parent factory model.
from ..Factory.notif_factory import Creator
from ..Interface.notif_interface import Product
from ..Product.email_notif import EmailNotifier

class EmailNotifierFactory(Creator):

    def _factory_method(self) -> Product:
        return EmailNotifier()