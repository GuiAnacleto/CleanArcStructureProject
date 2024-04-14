import re
from abc import ABC, abstractmethod

class CustomerInterface(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_cpf(self) -> str:
        pass

    @abstractmethod
    def get_email(self) -> str:
        pass

    @abstractmethod
    def set_email(self, email: str) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class Customer(CustomerInterface):
    def __init__(self, name: str, cpf: str, email: str):
        if not self.__isValidCpf(cpf): raise ValueError("CPF inválido. O cliente não pode ser criado.")
        self.__name = name
        self.__cpf = self.__set_cpf(cpf)
        self.__email = email

    def get_name(self) -> str:
        return self.__name
    
    def get_cpf(self) -> str:
        return self.__cpf

    def get_email(self) -> str:
        return self.__email
    
    def __set_cpf(self, cpf: str) -> str:
        return re.sub(r'[^0-9]', '', cpf)
    
    def set_email(self, email: str) -> None:
        self.__email = email
    
    def __str__(self, ) -> str:
        return f"Customer(Name: {self.__name}, CPF: {self.__cpf}, E-mail: {self.__email})"

    def __isValidCpf(self, cpf: str) -> bool:
        cpf = re.sub(r'[^0-9]', '', cpf)
        if len(cpf) != 11: return False
        if cpf == cpf[0] * 11: return False
        cpf = list(map(int, cpf))
        sum1 = sum(cpf[i] * (10 - i) for i in range(9))
        digit1 = (sum1 * 10) % 11 if sum1 % 11 >= 2 else 0
        sum2 = sum(cpf[i] * (11 - i) for i in range(10))
        digit2 = (sum2 * 10) % 11 if sum2 % 11 >= 2 else 0            
        if digit1 == cpf[9] and digit2 == cpf[10]: return True 
        else: return False