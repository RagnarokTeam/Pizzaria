# """
# Data........: 2020-05-16
# Projeto.....: Pizzaria-Ragnarok
# Arquivo.....: criacaoTabelas.py
# Descrição...: Criacao de tabelas no SQLite
# Autor.......: Camila A. Oliveira - Eq. Ragnarok
# Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
#
# Referencias:
# ""

import os
import sqlite3

# definindo um arquivo para as tabelas
fileDB = 'C:\\Users\Family\Documents\GitHub\LUL\Pizzaria\src\db\hela.sqlite'

# excluindo o arquivo de banco de dados
print('Excluindo o arquivo de banco de dados, caso exista.')
if os.path.exists(fileDB):
    os.remove(fileDB)
else:
    print(f'O arquivo: {fileDB} não existe!')

# Criando a base de dados
print(f'Criado um novo arquivo {fileDB}')
connection = sqlite3.connect(fileDB)

# Get a cursor object
cursor = connection.cursor()


# Criacao de tabelas

def tab_cliente():
    cursor.execute('CREATE TABLE IF NOT EXISTS cliente \
                   (CODIGO_CLI  INTEGER     NOT NULL   PRIMARY KEY AUTOINCREMENT ,                     TEL_FIXO string(15),                     TEL_CEL string(15),                     NOME_CLI string(40),                     ENDERECO string(30),                     NR_END string(10),                     COMPLEMENTO string(25),                     BAIRRO string(20),                     CIDADE string(20),                     UF string(02))'
                   )


tab_cliente()


def tab_pizza():
    cursor.execute('CREATE TABLE IF NOT EXISTS pizza \
                    (CODIGO_PIZ    INTEGER  NOT NULL    PRIMARY KEY AUTOINCREMENT ,                     DATA_CRIACAO date,                     DATA_INATIVACAO date,                     NOME_PIZ string(100),                     INGREDIENTES text,                     VALOR_CUSTO numeric(10, 2))'
                   )


tab_pizza()


def tab_pedido():
    cursor.execute('CREATE TABLE IF NOT EXISTS pedido \
                    (COD_PEDIDO     INTEGER NOT NULL    PRIMARY KEY AUTOINCREMENT ,                     DATA_PED date,                     HORA_PED time,                     CODIGO_CLI integer,                     TOTAL_PED numeric(10, 2))'
                   )


tab_pedido()


def itens_pedido():
    cursor.execute('CREATE TABLE IF NOT EXISTS itens_pedido \
                    (COD_PED    INTEGER     NOT NULL,                     ITEM integeR NOT NULL,                     CODIGO_PIZ integer,                     TAMANHO string(10))'
                   )


itens_pedido()
