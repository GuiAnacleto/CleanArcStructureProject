import sqlite3
from app.entities.Customer import Customer


class Supermarket:
    def saveCustomer(self, customer: Customer) -> None:
        try:
            conn = sqlite3.connect('supermarket.db')
            cursor = conn.cursor()
            query = "INSERT INTO customers (name, cpf, email) VALUES (?, ?, ?)"
            cursor.execute(query, (customer.get_name(), customer.get_cpf(), customer.get_email()))
            conn.commit()
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Erro ao inserir cliente no banco de dados: {e}")
        finally:
            conn.close()

    def getCustomer(self, identifier) -> Customer:
        try:
            conn = sqlite3.connect('supermarket.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers WHERE customer_id = ? OR cpf = ?", (identifier, identifier))
            customer_data = cursor.fetchone()
            return Customer(customer_data[1], customer_data[2], customer_data[3]) if customer_data else None
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Erro ao obter cliente do banco de dados: {e}")
        finally:
            conn.close()