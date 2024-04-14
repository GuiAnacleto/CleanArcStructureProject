import pytest
from faker import Faker
from app.entities.Customer import Customer, CustomerInterface
from infraestructure.db.supermarket_database import Supermarket

def test_supermarket_save_get_customer():
    # Arrange
    fake = Faker('pt_Br')
    name, cpf, email = fake.name(), fake.cpf(), fake.email() 
    supermarket = Supermarket()
    customer: CustomerInterface = Customer(name, cpf, email)
    # Act
    supermarket.saveCustomer(customer)
    # Assert
    supermarketCustumerReturn = supermarket.getCustomer(customer.get_cpf())
    assert supermarketCustumerReturn.get_name() == customer.get_name()
    assert supermarketCustumerReturn.get_cpf() == customer.get_cpf()
    assert supermarketCustumerReturn.get_email() == customer.get_email()

def test_supermarket_save_customer_error():
    # Arrange
    fake = Faker('pt_Br')
    name, cpf, email = fake.name(), fake.cpf(), fake.email() 
    supermarket = Supermarket()
    customer: CustomerInterface = Customer(name, cpf, email)
    supermarket.saveCustomer(customer)
    # Act
    result = supermarket.saveCustomer(customer)
    # Assert
    assert result == "Cliente ja cadastrado."