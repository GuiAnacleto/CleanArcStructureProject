import uuid
from abc import ABC, abstractmethod

class ProductInterface(ABC):
    @abstractmethod
    def getId(self, ) -> int: pass

    @abstractmethod
    def getName(self, ) -> str: pass

    @abstractmethod
    def getPrice(self, ) -> float: pass

    @abstractmethod
    def getQuantity(self, ) -> int: pass

    @abstractmethod
    def setName(self, name: str) -> None: pass
    
    @abstractmethod
    def setPrice(self, price: float) -> None: pass

    @abstractmethod
    def setQuantity(self, quantity: int) -> int: pass
    
    @abstractmethod
    def increaseQuantity(self, ) -> int: pass
    
    @abstractmethod
    def decreaseQuantity(self, ) -> int: pass

class Product(ProductInterface):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__product_id: str(uuid.uuid4()) # type: ignore
        self.__name: name
        self.__price: price
        self.__quantity: quantity

    def getId(self, ) -> int: return self.__product_id

    def getName(self, ) -> str: return self.__name

    def getPrice(self, ) -> float: return self.__price

    def getQuantity(self, ) -> int: return self.__quantity

    def setName(self, name: str) -> None: 
        if len(name) < 3: return "O nome do produto deve ser maior que 2 caracteres."
        new_name: self.__name = name
        return new_name

    def setPrice(self, price: float) -> None: 
        if price < 0: return "O preço deve ser maior ou igual a 0."
        new_price: self.__price = price  
        return new_price

    def setQuantity(self, quantity: int) -> int: 
        if quantity <= 0: return "A quantidade de itens não pode ser menor que 0."
        new_quantity: self.__quantity = quantity
        return new_quantity

    def increaseQuantity(self, ) -> int:
        new_quantity: self.__quantity = self.__quantity + 1
        return new_quantity
    
    def decreaseQuantity(self, ) -> int:
        if self.__quantity <= 0: return "A quantidade de itens ja é 0."
        new_quantity: self.__quantity = self.__quantity - 1
        return new_quantity
    

