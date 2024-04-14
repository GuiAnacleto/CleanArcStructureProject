import pytest
from faker import Faker
from app.entities.Customer import Customer, CustomerInterface
from infraestructure.db.supermarket_database import Supermarket

def test_supermarket_get_customer():
    # Arrange
    fake = Faker('pt_Br')
    name, cpf, email = fake.name(), fake.cpf(), fake.email() 
    supermarket = Supermarket()
    customer: CustomerInterface = Customer(name, cpf, email)
    # Act
    supermarket.saveCustomer(customer)
    # Assert
    supermarketCustumerReturn = supermarket.getCustomer(customer.get_Id())
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

def test_get_all_customers():
    # Arrange
    supermarket = Supermarket()

    # Act
    customers = supermarket.getAllCustomers()

    # Assert
    assert customers
    assert len(customers) > 1

def test_delete_customer_sucess():
    # Arrange
    fake = Faker('pt_Br')
    name, cpf, email = fake.name(), fake.cpf(), fake.email() 
    supermarket = Supermarket()
    customer: CustomerInterface = Customer(name, cpf, email)
    supermarket.saveCustomer(customer)

    # Act
    result = supermarket.deleteCustomer(customer.get_Id())

    # Assert
    assert result == f"Usuario [{customer.get_Id()}] deletado com sucesso."

def test_update_customer_sucess():
    # Arrange
    fake = Faker('pt_Br')
    name, cpf, email = fake.name(), fake.cpf(), fake.email() 
    supermarket = Supermarket()
    customer: CustomerInterface = Customer(name, cpf, email)
    supermarket.saveCustomer(customer)

    # Act
    result = supermarket.updateCustomerEmail(customer.get_Id(), fake.email())

    # Assert
    assert result == f"Usuario [{customer.get_Id()}] alterado com sucesso."