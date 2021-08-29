from ..Interface.notif_interface import Product

class SmsNotifier(Product):

    def notify(self) -> str:
        return "SMS sent."