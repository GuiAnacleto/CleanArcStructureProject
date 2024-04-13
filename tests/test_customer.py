import pytest
from app.entities.Customer import Customer

def test_get_name():
    customer = Customer("João", "12345678909", "joao@example.com")
    assert customer.get_name() == "João"

def test_get_cpf():
    customer = Customer("Maria", "98765432100", "maria@example.com")
    assert customer.get_cpf() == "98765432100"

def test_get_email():
    customer = Customer("Pedro", "98765432100", "pedro@example.com")
    assert customer.get_email() == "pedro@example.com"

def test_set_email():
    customer = Customer("Ana", "98765432100", "ana@example.com")
    customer.set_email("ana@gmail.com")
    assert customer.get_email() == "ana@gmail.com"

def test_create_customer_sucess():
    # Arrange
    name = "Alice"
    cpf = "98765432100"
    email = "alice@example.com"

    # Act
    customer = Customer(name, cpf, email)

    # Assert
    assert customer.get_name() == name
    assert customer.get_cpf() == cpf
    assert customer.get_email() == email

def test_create_customer_error():
    # Arrange
    name = "Alice"
    cpf = "abobora"
    email = "alice@example.com"

    # Act
    with pytest.raises(ValueError) as exc_info:
        customer = Customer(name, cpf, email)

    # Assert
    assert str(exc_info.value) == "CPF inválido. O cliente não pode ser criado."