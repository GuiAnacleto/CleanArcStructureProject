from app.entities.Customer import Customer, CustomerInterface
from infraestructure.db.supermarket_database import Supermarket, SupermarketInterface

class inputDto:
    clientName = str
    clientCPF = str
    clientEmail = str

class outputDto:
    cliente = Customer

def mapper(customer: Customer) -> inputDto:
    inputDto.clientName = customer.get_name()
    inputDto.clientCPF = customer.get_cpf()
    inputDto.clientEmail = customer.get_email()
    return inputDto

def execute(input: inputDto) -> outputDto:
    customer: CustomerInterface = Customer(input.clientName, input.clientCPF, input.clientEmail)
    supermarketDb: SupermarketInterface = Supermarket()
    supermarketDb.saveCustomer(customer=customer)
    return supermarketDb.getCustomer(customer.get_Id())

