import sqlite3

# Função para deletar o banco de dados
def deletar_banco_dados():
    # Conecta ao banco de dados (ou cria um novo se não existir)
    conn = sqlite3.connect('supermarket.db')

    # Cria um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Desabilita temporariamente o suporte a chaves estrangeiras para deletar o banco de dados
    cursor.execute("PRAGMA foreign_keys = OFF;")

    # Deleta o banco de dados, se existir
    cursor.execute('DROP DATABASE IF EXISTS supermarket.db;')

    # Reabilita o suporte a chaves estrangeiras
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Commit e fecha a conexão
    conn.commit()
    conn.close()

# Deletar o banco de dados
deletar_banco_dados()