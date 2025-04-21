from datetime import date
from app.domain.apolice import Apolice
from app.domain.cpf import CPF
from app.repositories.IApoliceRepository import IApoliceRepository

class ServicoCriarApolice:
    def __init__(self, repositorio: IApoliceRepository):
        self.repositorio = repositorio

    def executar(self, cpf: str, data_inicio: date, data_fim: date, premio: float) -> Apolice:

        #valida o CPF
        validado = CPF(cpf)

        #valida vigencia da apolice
        if data_inicio > data_fim:
            raise ValueError("A data de início deve ser anterior ou igual à data de fim.")
        
        #valida o valor do premio
        if premio <= 0:
            raise ValueError("O prêmio deve ser maior que zero.")
        
        # Cria a nova apólice 
        nova_apolice = Apolice(
            id=None,  # ID será gerado automaticamente
            cpf=validado.cpf, 
            data_inicio=data_inicio,
            data_fim=data_fim, 
            valor_premio=premio
        )

        #persistência da apolice
        self.repositorio.salvar(nova_apolice)
      
        return nova_apolice


