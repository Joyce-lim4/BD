import sqlite3

#1-conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

#2-excluisao de dados
id = (1,2)
cursor.execute(
    """
    DELETE FROM filmes
    WHERE ID in (?,?)
    """,
    id
)
