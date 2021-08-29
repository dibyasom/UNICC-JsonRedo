# Importing dependecnies and parent factory model.
from ..Factory.notif_factory import Creator
from ..Interface.notif_interface import Product
from ..Product.sms_notif import SmsNotifier


class SmsNotifierFactory(Creator):

    def _factory_method(self) -> Product:
        return SmsNotifier()
