# Importing dependecnies and parent factory model.
from ..Factory.notif_factory import Creator
from ..Interface.notif_interface import Product
from ..Product.post_notif import PostNotifier

class PostNotifierFactory(Creator):

    def _factory_method(self) -> Product:
        return PostNotifier()