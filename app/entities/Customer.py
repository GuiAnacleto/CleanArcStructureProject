import re

class Customer:
    def __init__(self, name: str, cpf: str, email: str):
        if not self.__isValidCpf(cpf): raise ValueError("CPF inválido. O cliente não pode ser criado.")
        self.__name = name
        self.__cpf = cpf
        self.__email = email

    def get_name(self) -> str:
        return self.__name

    def get_cpf(self) -> str:
        return self.__cpf

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str) -> None:
        self.__email = email

    def __isValidCpf(self, cpf: str) -> bool:
        # Remover caracteres não numéricos do CPF
        cpf = re.sub(r'[^0-9]', '', cpf)

        # Verificar se o CPF possui 11 dígitos
        if len(cpf) != 11:
            return False

        # Verificar se todos os dígitos são iguais (caso comum de CPF inválido)
        if cpf == cpf[0] * 11:
            return False

        # Calcular dígitos verificadores
        cpf = list(map(int, cpf))
        sum1 = sum(cpf[i] * (10 - i) for i in range(9))  # Primeiros 9 dígitos
        digit1 = (sum1 * 10) % 11 if sum1 % 11 >= 2 else 0

        sum2 = sum(cpf[i] * (11 - i) for i in range(10))  # Todos os 10 dígitos
        digit2 = (sum2 * 10) % 11 if sum2 % 11 >= 2 else 0

        # Verificar os dígitos verificadores
        if digit1 == cpf[9] and digit2 == cpf[10]:
            return True
        else:
            return False