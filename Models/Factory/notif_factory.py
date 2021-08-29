# Importing dependencies.
from __future__ import annotations
from abc import ABC, abstractmethod

from ..Interface.notif_interface import Product

class Creator(ABC):

    @abstractmethod
    def _factory_method(self):
        pass

    def notify_job(self) -> str:

        product: Product = self._factory_method()
        return product.notify()
