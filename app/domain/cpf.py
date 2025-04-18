import re

class Cpf:
    def __init__(self, cpf: str) -> None:
        self._cpf = cpf
        self.__validate_cpf()

    def __validate_cpf(self) -> None:
        """Validates the CPF number."""
        if not self._cpf:
            raise ValueError('O CPF não pode ser vazio.')
        if not re.fullmatch(r'\d{11}', self._cpf):  # Validate if the CPF is a number with 11 digits
            raise ValueError('Formato de CPF inválido. O CPF deve conter 11 dígitos.')
        self.__validate_cpf_digits()  # Validate if the CPF is valid

    def __validate_cpf_digits(self) -> None:
        """Validates the CPF check digits."""
        # Implementação simplificada para validação dos dígitos verificadores
        cpf = [int(digit) for digit in self._cpf]
        for i in range(9, 11):
            value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
            check_digit = (value * 10 % 11) % 10
            if check_digit != cpf[i]:
                raise ValueError('CPF inválido.')

    @property
    def cpf(self) -> str:
        """Returns the validated CPF."""
        return self._cpf


# Teste básico

try:
    teste = Cpf('12345678909')
    print(teste.cpf)
except ValueError as e:
    print(f"Erro: {e}")