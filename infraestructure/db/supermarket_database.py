import sqlite3
from abc import ABC, abstractmethod
from app.entities.Customer import Customer, CustomerInterface

class SupermarketInterface(ABC):

    @abstractmethod
    def saveCustomer(self, customer: CustomerInterface) -> None: pass

    @abstractmethod
    def getCustomer(self, identifier) -> Customer: pass
    
    @abstractmethod
    def updateCustomerEmail(self, customerId: str, email: str) -> str: pass

    @abstractmethod
    def deleteCustomer(self, identifier) -> str: pass

    @abstractmethod
    def getAllCustomers(self, ) -> dict: pass

class Supermarket(SupermarketInterface):
    def saveCustomer(self, customer: CustomerInterface) -> None:
        if self.getCustomer(customer.get_cpf()) != None: return "Cliente ja cadastrado."
        try:            
            conn = sqlite3.connect('supermarket.db')
            cursor = conn.cursor()
            query = "INSERT INTO customers (customer_id, name, cpf, email) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (customer.get_Id(), customer.get_name(), customer.get_cpf(), customer.get_email()))
            conn.commit()
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Erro ao inserir cliente no banco de dados: {e}")
        finally:
            conn.close()

    def getCustomer(self, identifier) -> Customer:
        try:
            conn = sqlite3.connect('supermarket.db')
            cursor = conn.cursor()
            cursor.execute("SELECT name, cpf, email FROM customers WHERE customer_id = ? OR cpf = ?", (identifier, identifier))
            customer_data = cursor.fetchone()
            return Customer(customer_data[0], customer_data[1], customer_data[2]) if customer_data else None
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Erro ao obter cliente do banco de dados: {e}")
        finally:
            conn.close()
    
    def updateCustomerEmail(self, customerId: str, email: str) -> str:
        try:
            conn = sqlite3.connect('supermarket.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE customers SET email = ? WHERE customer_id = ?", (email, customerId))
            return f"Usuario [{customerId}] alterado com sucesso."
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Erro ao alterar cliente do banco de dados: {e}")
        finally:
            conn.commit()
            conn.close()

    def deleteCustomer(self, identifier) -> str:
        try:
            conn = sqlite3.connect('supermarket.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM customers WHERE customer_id = ? OR cpf = ?", (identifier, identifier))
            return f"Usuario [{identifier}] deletado com sucesso."
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Erro ao deletar cliente do banco de dados: {e}")
        finally:
            conn.close()

    def getAllCustomers(self, ) -> dict:
        try:
            conn = sqlite3.connect('supermarket.db')
            cursor = conn.cursor()
            cursor.execute("SELECT name, cpf, email FROM customers")
            customer_dict = cursor.fetchall()
            return customer_dict
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Erro ao obter cliente do banco de dados: {e}")
        finally:
            conn.close()