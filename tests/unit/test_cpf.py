import pytest
from app.domain.cpf import Cpf

def test_valid_cpf():
    cpf = Cpf("12345678909")
    assert cpf.cpf == "12345678909"

def test_empty_cpf():
    with pytest.raises(ValueError, match="O CPF não pode ser vazio."):
        Cpf("")

def test_invalid_format_cpf():
    with pytest.raises(ValueError, match="Formato de CPF inválido. O CPF deve conter 11 dígitos."):
        Cpf("12345")

def test_invalid_cpf_digits():
    with pytest.raises(ValueError, match="CPF inválido."):
        Cpf("12345678900")