import pytest
from datetime import date
from uuid import uuid4
from app.domain.apolice import Apolice
from app.domain.cpf import CPF

def test_apolice_vigente():
    apolice = Apolice(
        id=uuid4(),
        cpf="12345678909",
        data_inicio=date(2023, 1, 1),
        data_fim=date(2027, 1, 1),
        valor_premio=1000.0
    )
    assert apolice.esta_Vigente() is True

def test_apolice_nao_vigente():
    apolice = Apolice(
        id=uuid4(),
        cpf="12345678909",
        data_inicio=date(2022, 1, 1),
        data_fim=date(2022, 12, 31),
        valor_premio=1000.0
    )
    assert apolice.esta_Vigente() is False

def test_data_inicio_maior_que_data_fim():
    with pytest.raises(ValueError, match="A data de início deve ser anterior ou igual à data de fim."):
        Apolice(
            id=uuid4(),
            cpf="12345678909",
            data_inicio=date(2024, 1, 1),
            data_fim=date(2023, 1, 1),
            valor_premio=1000.0
        )