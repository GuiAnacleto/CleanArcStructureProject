import sqlite3

def drop_tables():
    try:
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect('supermarket.db')
        cursor = conn.cursor()

        # Listar todas as tabelas no banco de dados
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Para cada tabela encontrada, emitir um comando DROP TABLE
        for table in tables:
            table_name = table[0]
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            print(f"Tabela {table_name} removida com sucesso.")

        print("Todas as tabelas foram removidas do banco de dados.")

    except sqlite3.Error as e:
        print(f"Erro ao remover tabelas do banco de dados: {e}")

    finally:
        # Fechar a conexão com o banco de dados
        conn.close()

# Chamada da função para remover todas as tabelas do banco de dados
drop_tables()