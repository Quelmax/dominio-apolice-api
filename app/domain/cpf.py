import re

class CPF:
    def __init__(self, cpf: str) -> None:
        self._cpf = cpf
        self.__validar_cpf()

    def __validar_cpf(self) -> None:
        """Valida o formato e os dígitos do CPF."""

        if not self._cpf:
            raise ValueError('O CPF não pode ser vazio.')
        if not re.fullmatch(r'\d{11}', self._cpf):  # Valida se o CPF contém apenas dígitos e tem 11 caracteres
            raise ValueError('Formato de CPF inválido. O CPF deve conter 11 dígitos.')
        self.__validar_cpf_digitos() 

    def __validar_cpf_digitos(self) -> None:
        """Valida os dígitos verificadores do CPF."""
        # Implementação simplificada para validação dos dígitos verificadores
        cpf = [int(digit) for digit in self._cpf]
        for i in range(9, 11):
            value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
            check_digit = (value * 10 % 11) % 10
            if check_digit != cpf[i]:
                raise ValueError('CPF inválido.')

    @property
    def cpf(self) -> str:
        """Retorna o CPF validado."""
        return self._cpf


# Teste básico

# try:
#     teste = CPF('12345678909')
#     print(teste.cpf)
# except ValueError as e:
#     print(f"Erro: {e}")