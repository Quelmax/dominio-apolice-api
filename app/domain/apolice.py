from datetime import date
from uuid import uuid4, UUID
from app.domain.cpf import CPF

class Apolice:
    def __init__(self, id: UUID, cpf: str, data_inicio: date, data_fim: date, valor_premio: float):
        self.id = uuid4()
        self.cpf = CPF(cpf)
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.valor_premio = valor_premio

        if self.data_inicio > self.data_fim:
            raise ValueError("A data de início deve ser anterior ou igual à data de fim.")

    def esta_Vigente(self) -> bool:
        """Verifica se a apólice está vigente."""
        data_atual = date.today()
        return self.data_inicio <= data_atual <= self.data_fim
