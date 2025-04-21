import pytest
from app.domain.cpf import CPF

def test_valid_cpf():
    cpf = CPF("12345678909")
    assert cpf.cpf == "12345678909"

def test_empty_cpf():
    with pytest.raises(ValueError, match="O CPF não pode ser vazio."):
        CPF("")

def test_invalid_format_cpf():
    with pytest.raises(ValueError, match="Formato de CPF inválido. O CPF deve conter 11 dígitos."):
        CPF("12345")

def test_invalid_cpf_digits():
    with pytest.raises(ValueError, match="CPF inválido."):
        CPF("12345678900")