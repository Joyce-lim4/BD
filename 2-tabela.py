import sqlite3

# 1 - Conectando ao banco de dados
conexao = sqlite3.connect('titulo.db')

# 2 - Criando o cursor
cursor = conexao.cursor()

# 3 - Criando a tabela (se ainda não existir)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        nota REAL NOT NULL
    );
""")

# 4 - Confirmando alterações e fechando a conexão
conexao.commit()
conexao.close()

print("Tabela foi criada (ou já existia)")
