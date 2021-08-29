from ..Interface.notif_interface import Product

class EmailNotifier(Product):

    def notify(self) -> str:
        return "Email sent."
