import json
from app.entities.Customer import *

def jsonToCustomer(jsonCustomer: json) -> Customer:
    return Customer(jsonCustomer.get('name'), jsonCustomer.get('CPF'), jsonCustomer.get('email'))
