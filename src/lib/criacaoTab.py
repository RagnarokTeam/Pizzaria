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

from src.db.Asgard import Bifrost


# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()


# Criacao de tabelas
# "Dropando a tabela caso exista"
cursor.execute('DROP TABLE IF EXISTS employee')


def tab_cliente():
    cursor.execute('CREATE TABLE IF NOT EXISTS cliente \
                   (CODIGO_CLI  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, TEL_FIXO string(15), \
                   TEL_CEL string(15), NOME_CLI string(40), ENDERECO string(30), NR_END string(10), \
                    COMPLEMENTO string(25), BAIRRO string(20), CIDADE string(20), UF string(02),DATA_CADASTRO date, DATA_INATIVO date)'
                   )

tab_cliente()

# "Dropando a tabela caso exista"
#cursor.execute('DROP TABLE IF EXISTS employee')


def tab_pizza():
    cursor.execute('CREATE TABLE IF NOT EXISTS pizza \
                    (CODIGO_PIZ    INTEGER  NOT NULL    PRIMARY KEY AUTOINCREMENT,\
                     TIPO_PIZ string(8), DATA_CRIACAO date,\
                     DATA_INATIVACAO date, NOME_PIZ string(100), '
                   'INGREDIENTES text, VALOR_CUSTO numeric(10, 2))'
                   )


tab_pizza()

# "Dropando a tabela caso exista"
cursor.execute('DROP TABLE IF EXISTS employee')


def tab_pedido():
    cursor.execute('CREATE TABLE IF NOT EXISTS PEDIDO (COD_PED	INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,DATA_PED		DATE,\
	HORA_PED		TIME,\
	CODIGO_CLI		INTEGER,\
	TOTAL_PED		NUMERIC(10,2),\
	CONSTRAINT FK_PEDIDO_CODIGOCLI FOREIGN KEY(CODIGO_CLI) REFERENCES CLIENTE(CODIGO_CLI)\
);')


tab_pedido()

# "Dropando a tabela caso exista"
cursor.execute('DROP TABLE IF EXISTS employee')


def itens_pedido():
    cursor.execute('CREATE TABLE IF NOT EXISTS ITENS_PEDIDO (\
	COD_PED			INTEGER NOT NULL,\
	ITEM			INTEGER NOT NULL,\
	CODIGO_PIZ		INTEGER,\
	TAMANHO			STRING (10),\
	CONSTRAINT PK_ITENSPEDIDO PRIMARY KEY(COD_PED, ITEM),\
	CONSTRAINT FK_ITENSPEDIDO_CODIGOPIZ FOREIGN KEY(CODIGO_PIZ) REFERENCES PIZZA(CODIGO_PIZ));')


itens_pedido()
print('Tabelas criadas com sucesso!')

# fechando conecção
Bifrost.connection.close()
