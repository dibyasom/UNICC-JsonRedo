from ..Interface.notif_interface import Product

class PostNotifier(Product):

    def notify(self) -> str:
        return "API called."
