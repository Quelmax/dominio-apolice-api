from abc import ABC, abstractmethod
from app.domain.apolice import Apolice

class IApoliceRepository(ABC):
    @abstractmethod
    def salvar(self, apolice: Apolice) -> None:
        """
        Salva a apólice no repositório.
        :param apolice: A apólice a ser salva.
        """
        pass