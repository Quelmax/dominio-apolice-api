from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date
from uuid import UUID
from app.services.servico_criar_apolice import ServicoCriarApolice
from app.repositories.repositorio_memoria_mock import ApoliceRepositorioMemoriaMock

rota = APIRouter()
repositorio = ApoliceRepositorioMemoriaMock()
servico = ServicoCriarApolice(repositorio=repositorio)

class ApoliceRequest(BaseModel):
    cpf: str
    data_inicio: date
    data_fim: date
    valor_premio: float

class ApoliceResponse(BaseModel):
    id: UUID  
    cpf: str
    data_inicio: date
    data_fim: date
    valor_premio: float


@rota.post(
    "/apolice",
    response_model=ApoliceResponse,
    status_code=201,
    description="Cria uma nova apólice de seguro com os dados fornecidos."
)
async def criar_apolice(apolice: ApoliceRequest):
    try:
        apolice_criada = servico.executar(
            cpf=apolice.cpf,
            data_inicio=apolice.data_inicio,
            data_fim=apolice.data_fim,
            premio=apolice.valor_premio
            )

        print(f"Dados recebidos: {apolice}")
        print(f"Apolice criada: {apolice_criada.id}")

        return ApoliceResponse(
            id=apolice_criada.id,
            cpf=apolice_criada.cpf.cpf,
            data_inicio=apolice_criada.data_inicio,
            data_fim=apolice_criada.data_fim,
            valor_premio=apolice_criada.valor_premio
        )  
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:# Log da exceção para depuração
        print(f"Erro interno: {e}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")