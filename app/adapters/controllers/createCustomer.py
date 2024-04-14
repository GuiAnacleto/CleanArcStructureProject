from app.use_cases.CreateCustomer import *
from app.adapters.adapters.JsonToCustomer import *

def createCustomer(customer: any) -> outputDto:
    customerObj = jsonToCustomer(customer)
    inputDto = mapper(customerObj)
    return execute(inputDto)