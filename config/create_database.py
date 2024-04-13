import sqlite3

# Função para criar o banco de dados e tabelas
def criar_banco_dados():
    # Conecta ao banco de dados (ou cria um novo se não existir)
    conn = sqlite3.connect('supermarket.db')

    # Cria um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Define o suporte a chaves estrangeiras
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Criação das tabelas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            sale_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            sale_date DATE NOT NULL,
            total_amount REAL NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sale_items (
            sale_item_id INTEGER PRIMARY KEY,
            sale_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            total_price REAL NOT NULL,
            FOREIGN KEY (sale_id) REFERENCES sales(sale_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    ''')

    # Commit e fecha a conexão
    conn.commit()
    conn.close()

# Criar o banco de dados e tabelas
criar_banco_dados()