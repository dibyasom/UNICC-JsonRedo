# Importing dependencies.
from __future__ import annotations
from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def notify(self) -> str:
        pass