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
    def listar(self) -> list[Apolice]:
        """
        Lista todas as apólices no repositório.
        :return: Uma lista de apólices.
        """
        pass