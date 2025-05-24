import sqlite3

#1- conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

#2- inserindo dados
cursor.execute(
    """
        INSERT INTO filmes(nome, ano, nota)
        VALUES ('Sonic', 2020, 8)
    """
)

conexao.commit()
conexao.close()
print("Dados inseridos na tabela")
