import sqlite3

#1- conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

#2-atualiizando dados
id = 1
cursor.execute(
    """
        UPDATE filmes SET nome = ?
        WHERE id = ?
    """,
    ("Batmam", id)

)

conexao.commit()
print("Dados atualizados")