from domain.apolice import Apolice

class IApoliceRepository:
    def salvar(self, apolice: Apolice) -> None:
        """
        Salva a apólice no repositório. 
        :param apolice: A apólice a ser salva.
        """
        raise NotImplementedError("Esse método deve ser implementado na subclasse.")