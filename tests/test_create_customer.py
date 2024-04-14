import json
from app.adapters.controllers.createCustomer import createCustomer
from faker import Faker

def test_create_customer_sucess():
    #Arrange
    fake = Faker('pt_Br')
    name, cpf, email = fake.name(), fake.cpf(), fake.email() 
    data = {
        "name": name,
        "CPF": cpf,
        "email": email
    }

    #Act
    result = createCustomer(data)

    #Assert
    assert result.get_name() == name