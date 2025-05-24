import sqlite3

#1-conctando no BD
conexao = sqlite3.connect('titulo.db')
cursor= conexao.cursor()

#2-leitura de dados
dados = cursor.execute("SELECT * FROM filmes")

print(dados.fetchall())
