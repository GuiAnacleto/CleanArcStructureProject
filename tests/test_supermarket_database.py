import pytest
from app.entities.Customer import Customer
from infraestructure.db.supermarket_database import Supermarket

def test_get_name():
    # Arrange
    supermarket = Supermarket()
    customer = Customer("João", "12345678909", "joao4@example.com")
    # Act
    supermarket.saveCustomer(customer)
    # Assert
    supermarketCustumerReturn = supermarket.getCustomer(12345678909)
    assert supermarketCustumerReturn.get_name() == customer.get_name()
    assert supermarketCustumerReturn.get_cpf() == customer.get_cpf()
    assert supermarketCustumerReturn.get_email() == customer.get_email()