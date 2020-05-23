# """
# Data........: 2020-05-23
# Projeto.....: Pizzaria-Ragnarok
# Arquivo.....: cadastroClientes.py
# Descrição...: Cadastro dos Clientes no SQLite
# Autor.......: Paula Tanaka - Eq. Ragnarok
# Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
#
# Referencias:
# ""


from src.db.Asgard import Bifrost


# variavel "cursor" pode ser alterada para qualquer outro nome de sua escolha
cursor = Bifrost.connection.cursor()


def cad_cliente():  # função que cadastra as pizzas do cardápio

    lista_clientes = [( '1','1', 'Paula', 'Rua Anfibólios', '562', 'NULL', 'Bonfim','Belo Horizonte','MG'),
                   ( '2','2', 'Camila', 'Parque Anhangabaú', '82', 'NULL', 'Centro', 'São Paulo', 'SP'),
                   ( '3','3', 'Jefferson', 'Rua Condado', '585', 'Ap 76 BL 5', 'Cavalhada','Porto Alegre','RS'),
                   ( '4','4', 'Jonathan','Rua Álvaro Anes', '90', 'NULL', 'Pinheiros','São Paulo','SP')]

    cursor.executemany("INSERT INTO cliente( TEL_FIXO, TEL_CEL, NOME_CLI, ENDERECO, NR_END,COMPLEMENTO,BAIRRO,CIDADE,UF) \
                    values (?,?,?,?,?,?,?,?,?)", lista_clientes)

    cursor.connection.commit()
    print('Dados inseridos com sucesso!')


# Chamada da funcao de inserção de dados
cad_cliente()

# fechando conexão
cursor.connection.close()
