# importando sqlite
import sqlite3 as lite 

#criando conexao
con = lite.connect('dados.db')

# criando tabela
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, hostname TEXT, mac TEXT, patrimonio TEXT, imagem TEXT)")