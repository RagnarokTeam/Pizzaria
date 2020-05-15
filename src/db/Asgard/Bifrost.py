"""
Data........: 2020-05-14
Projeto.....: RagnarokProject - Pizzaria
Arquivo.....: Bifrost.py
Descrição...: Conexão generalizada para toda a aplicação
Autor.......: Jefferson de Lima
Observações.: 2020-05-14 - [R00] Criação do Arquivo - Versao 1.00
              ...
Referencias:
"""


import os
import sqlite3

# definindo um arquivo para clientes
fileDB = 'C:\\Users\jeffe\git\PIZZARIA-RAGNAROK\src\db\cliente.sqlite'

# verificando se arquivo de banco de dados existe
print(f'Verificando se arquivo {fileDB} existe.')
if not os.path.exists(fileDB):
    print(f'O arquivo: {fileDB} não existe!')
    exit(-1)
else:
    pass

# Criando a base de dados
connection = sqlite3.connect(fileDB)
