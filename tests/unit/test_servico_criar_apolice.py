import pytest
from datetime import date
from unittest.mock import Mock
from app.services.servico_criar_apolice import ServicoCriarApolice
from app.domain.apolice import Apolice
from app.domain.cpf import CPF
from app.repositories.IApoliceRepository import IApoliceRepository
# from app.repositories.repositorio_memoria_mock import ApoliceRepositorioMemoriaMock as Mock

def test_criar_apolice_sucesso():
    # Mock do repositório
    repositorio_mock = Mock(spec=IApoliceRepository)

    # Instância do serviço
    servico = ServicoCriarApolice(repositorio=repositorio_mock)

    # Dados de entrada
    cpf = "05583711167"
    data_inicio = date(2025, 1, 1)
    data_fim = date(2027, 1, 1)
    premio = 1755.0


    # Executa o serviço
    apolice = servico.executar(cpf=cpf, data_inicio=data_inicio, data_fim=data_fim, premio=premio)

    # Verifica se a apólice foi criada corretamente
    assert isinstance(apolice, Apolice)
    assert apolice.cpf.cpf == cpf
    assert apolice.data_inicio == data_inicio
    assert apolice.data_fim == data_fim
    assert apolice.valor_premio == premio

    # Verifica se o método salvar foi chamado no repositório
    repositorio_mock.salvar.assert_called_once_with(apolice)

def test_criar_apolice_data_invalida():
    # Mock do repositório
    repositorio_mock = Mock(spec=IApoliceRepository)

    # Instância do serviço
    servico = ServicoCriarApolice(repositorio=repositorio_mock)

    # Dados de entrada com data inválida
    cpf = "12345678909"
    data_inicio = date(2024, 1, 1)
    data_fim = date(2023, 1, 1)
    premio = 1000.0

    # Verifica se o serviço levanta um erro para data inválida
    with pytest.raises(ValueError, match="A data de início deve ser anterior ou igual à data de fim."):
        servico.executar(cpf=cpf, data_inicio=data_inicio, data_fim=data_fim, premio=premio)

def test_criar_apolice_premio_invalido():
    # Mock do repositório
    repositorio_mock = Mock(spec=IApoliceRepository)

    # Instância do serviço
    servico = ServicoCriarApolice(repositorio=repositorio_mock)

    # Dados de entrada com prêmio inválido
    cpf = "12345678909"
    data_inicio = date(2023, 1, 1)
    data_fim = date(2024, 1, 1)
    premio = -100.0

    # Verifica se o serviço levanta um erro para prêmio inválido
    with pytest.raises(ValueError, match="O prêmio deve ser maior que zero."):
        servico.executar(cpf=cpf, data_inicio=data_inicio, data_fim=data_fim, premio=premio)